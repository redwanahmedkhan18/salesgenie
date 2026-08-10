import React from 'react';

interface SkeletonProps {
  className?: string;
  width?: string | number;
  height?: string | number;
  count?: number;
  variant?: 'text' | 'rect' | 'circle';
}

export function Skeleton({
  className = '',
  width,
  height,
  count = 1,
  variant = 'text',
}: SkeletonProps) {
  const baseClasses = 'animate-pulse bg-current rounded';
  const variantClasses = {
    text: 'rounded-sm',
    rect: 'rounded',
    circle: 'rounded-full',
  };

  const style: React.CSSProperties = {
    opacity: 0.3,
  };
  if (width) style.width = typeof width === 'number' ? `${width}px` : width;
  if (height) style.height = typeof height === 'number' ? `${height}px` : height;

  if (count > 1) {
    return (
      <>
        {Array.from({ length: count }).map((_, i) => (
          <span
            key={i}
            className={`${baseClasses} ${variantClasses[variant]} ${className} mb-1 last:mb-0`}
            style={style}
          />
        ))}
      </>
    );
  }

  return (
    <span
      className={`${baseClasses} ${variantClasses[variant]} ${className}`}
      style={style}
    />
  );
}

export function SkeletonTable({ rows = 3, columns = 4 }: { rows?: number; columns?: number }) {
  return (
    <div className="space-y-3">
      <div className="flex gap-2">
        {Array.from({ length: columns }).map((_, i) => (
          <Skeleton key={i} variant="text" height={20} />
        ))}
      </div>
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="flex gap-2">
          {Array.from({ length: columns }).map((_, j) => (
            <Skeleton key={j} variant="text" height={16} />
          ))}
        </div>
      ))}
    </div>
  );
}

export function SkeletonCard() {
  return (
    <div className="p-4 rounded-xl border" style={{ borderColor: 'var(--color-border)', background: 'var(--color-card)' }}>
      <Skeleton variant="text" height={24} className="mb-2 w-3/4" />
      <Skeleton variant="text" height={14} className="mb-2 w-full" />
      <Skeleton variant="text" height={14} className="mb-2 w-2/3" />
      <div className="flex gap-2 mt-3">
        <Skeleton variant="rect" width={60} height={24} />
        <Skeleton variant="rect" width={80} height={24} />
      </div>
    </div>
  );
}
