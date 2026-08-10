import { defineMiddleware, type MiddlewareResponse } from "astro:middleware";

const isDev = import.meta.env.DEV;

const DEV_CONNECT_SRC = [
  "'self'",
  "http://localhost:8001",
  "http://127.0.0.1:8001",
  "ws://localhost:8001",
  "ws://127.0.0.1:8001",
];

const PROD_CONNECT_SRC = ["'self'", "https:", "wss:"];

const connectSrc = isDev ? DEV_CONNECT_SRC : PROD_CONNECT_SRC;

const CSP_DIRECTIVES = [
  "default-src 'self'",
  "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://www.googletagmanager.com https://www.google-analytics.com",
  "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
  "img-src 'self' data: https: blob:",
  `connect-src ${connectSrc.join(" ")}`,
  "font-src 'self' https://fonts.gstatic.com",
  "frame-src 'self' https://accounts.google.com https://js.stripe.com",
  "object-src 'none'",
  "base-uri 'self'",
  "form-action 'self'",
  "frame-ancestors 'none'",
];

export const onRequest = defineMiddleware(async (context, next) => {
  const response: MiddlewareResponse = await next();

  const headers = new Headers(response.headers);

  headers.set("X-Frame-Options", "DENY");
  headers.set("X-Content-Type-Options", "nosniff");
  headers.set("Referrer-Policy", "strict-origin-when-cross-origin");
  headers.set("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=()");
  headers.set(
    "Strict-Transport-Security",
    "max-age=31536000; includeSubDomains; preload"
  );
  headers.set(
    "Content-Security-Policy",
    CSP_DIRECTIVES.join("; ")
  );

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
});
