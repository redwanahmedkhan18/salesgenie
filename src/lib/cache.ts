/**
 * In-memory response cache for frontend API calls.
 * Reduces duplicate network requests for static/reference data.
 */

interface CacheEntry<T> {
  data: T;
  timestamp: number;
  expiresAt: number;
}

const DEFAULT_TTL_MS = 5 * 60 * 1000; // 5 minutes

class APICache {
  private cache = new Map<string, CacheEntry<unknown>>();
  private maxSize = 100;

  set<T>(key: string, data: T, ttlMs: number = DEFAULT_TTL_MS): void {
    const now = Date.now();
    const entry: CacheEntry<T> = {
      data,
      timestamp: now,
      expiresAt: now + ttlMs,
    };

    if (this.cache.size >= this.maxSize) {
      const oldestKey = this.cache.keys().next().value;
      if (oldestKey) {
        this.cache.delete(oldestKey);
      }
    }

    this.cache.set(key, entry as CacheEntry<unknown>);
  }

  get<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) {
      return null;
    }

    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return null;
    }

    return entry.data as T;
  }

  has(key: string): boolean {
    const entry = this.cache.get(key);
    if (!entry) {
      return false;
    }

    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return false;
    }

    return true;
  }

  invalidate(key: string): void {
    this.cache.delete(key);
  }

  invalidatePattern(pattern: RegExp): void {
    for (const key of Array.from(this.cache.keys())) {
      if (pattern.test(key)) {
        this.cache.delete(key);
      }
    }
  }

  clear(): void {
    this.cache.clear();
  }

  size(): number {
    return this.cache.size;
  }
}

export const apiCache = new APICache();

  export const withCache = <T,>(key: string, ttlMs?: number) => {
    return (
      _target: unknown,
      _propertyKey: string,
      descriptor: TypedPropertyDescriptor<(...args: unknown[]) => Promise<T>>,
    ) => {
    const originalMethod = descriptor.value;
    if (!originalMethod) return descriptor;

    descriptor.value = async function (...args: unknown[]): Promise<T> {
      const cacheKey = `${key}:${JSON.stringify(args)}`;
      const cached = apiCache.get<T>(cacheKey);
      if (cached !== null) {
        return cached;
      }

      const result = await originalMethod.apply(this, args);
      apiCache.set(cacheKey, result, ttlMs);
      return result;
    };

    return descriptor;
  };
};
