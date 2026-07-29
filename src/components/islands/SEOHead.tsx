import React, { useEffect } from 'react';

interface SEOHeadProps {
  title?: string;
  description?: string;
  canonical?: string;
  openGraph?: {
    title?: string;
    description?: string;
    type?: string;
    image?: string;
    url?: string;
  };
  twitter?: {
    card?: string;
    site?: string;
    title?: string;
    description?: string;
    image?: string;
  };
  structuredData?: Record<string, unknown>;
}

export function SEOHead({
  title = 'SalesGenie - AI Customer Support & Sales Automation',
  description = 'SalesGenie is an enterprise AI platform that automates customer support, qualifies leads, and drives sales growth with AI agents.',
  canonical,
  openGraph,
  twitter,
  structuredData,
}: SEOHeadProps) {
  useEffect(() => {
    const setMeta = (name: string, content: string, isProperty = false) => {
      let meta = document.querySelector(
        isProperty ? `meta[property="${name}"]` : `meta[name="${name}"]`
      );
      
      if (!meta) {
        meta = document.createElement('meta');
        if (isProperty) {
          meta.setAttribute('property', name);
        } else {
          meta.setAttribute('name', name);
        }
        document.head.appendChild(meta);
      }
      meta.setAttribute('content', content);
    };

    const setLink = (rel: string, href: string) => {
      let link = document.querySelector(`link[rel="${rel}"]`);
      if (!link) {
        link = document.createElement('link');
        link.setAttribute('rel', rel);
        document.head.appendChild(link);
      }
      link.setAttribute('href', href);
    };

    setMeta('title', title);
    setMeta('description', description);
    
    if (canonical) {
      setLink('canonical', canonical);
    }

    const ogData = {
      title: openGraph?.title || title,
      description: openGraph?.description || description,
      type: openGraph?.type || 'website',
      image: openGraph?.image || 'https://salesgenie.ai/og-image.png',
      url: openGraph?.url || window.location.href,
      site_name: 'SalesGenie',
      locale: 'en_US',
    };

    setMeta('og:title', ogData.title, true);
    setMeta('og:description', ogData.description, true);
    setMeta('og:type', ogData.type, true);
    setMeta('og:image', ogData.image, true);
    setMeta('og:url', ogData.url, true);
    setMeta('og:site_name', ogData.site_name, true);
    setMeta('og:locale', ogData.locale, true);

    const twitterData = {
      card: twitter?.card || 'summary_large_image',
      site: twitter?.site || '@salesgenie',
      title: twitter?.title || ogData.title,
      description: twitter?.description || ogData.description,
      image: twitter?.image || ogData.image,
    };

    setMeta('twitter:card', twitterData.card);
    setMeta('twitter:site', twitterData.site);
    setMeta('twitter:title', twitterData.title);
    setMeta('twitter:description', twitterData.description);
    setMeta('twitter:image', twitterData.image);

    if (structuredData) {
      let script = document.querySelector('script[type="application/ld+json"]');
      if (!script) {
        script = document.createElement('script');
        script.setAttribute('type', 'application/ld+json');
        document.head.appendChild(script);
      }
      script.textContent = JSON.stringify(structuredData);
    }

    document.title = title;
  }, [title, description, canonical, openGraph, twitter, structuredData]);

  return null;
}

export interface BreadcrumbItem {
  name: string;
  url?: string;
}

export function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  if (!items || items.length === 0) return null;

  return (
    <nav 
      aria-label="Breadcrumb"
      className="breadcrumb"
      itemScope
      itemType="https://schema.org/BreadcrumbList"
    >
      <ol className="flex items-center space-x-2 text-sm">
        {items.map((item, index) => (
          <li 
            key={index} 
            itemProp="itemListElement" 
            itemScope 
            itemType="https://schema.org/ListItem"
          >
            <span className="flex items-center">
              {item.url ? (
                <a
                  href={item.url}
                  itemProp="item"
                  className="text-gray-600 hover:text-blue-600 transition-colors"
                >
                  <span itemProp="name">{item.name}</span>
                </a>
              ) : (
                <span 
                  className="text-gray-900 font-medium"
                  itemProp="name"
                  aria-current={index === items.length - 1 ? 'page' : undefined}
                >
                  {item.name}
                </span>
              )}
              {index < items.length - 1 && (
                <span className="text-gray-400 mx-2">/</span>
              )}
            </span>
          </li>
        ))}
      </ol>
    </nav>
  );
}