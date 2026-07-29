import React, { useEffect, useMemo } from 'react';

interface SEOProps {
  title?: string;
  description?: string;
  keywords?: string[];
  image?: string;
  url?: string;
  type?: 'website' | 'article' | 'product' | 'profile' | 'organization';
  author?: string;
  publishedTime?: string;
  modifiedTime?: string;
  locale?: string;
  noIndex?: boolean;
}

export function SEO({
  title = 'SalesGenie - AI Customer Support & Sales Automation',
  description = 'SalesGenie is an enterprise AI platform that automates customer support, qualifies leads, and drives sales growth with AI agents. Deploy in minutes with no coding required.',
  keywords = [
    'AI customer support',
    'AI sales agent',
    'lead qualification',
    'customer service automation',
    'enterprise AI',
    'chatbot',
    'sales automation',
    'RAG',
    'knowledge base',
  ],
  image = 'https://salesgenie.ai/og-image.png',
  url = 'https://salesgenie.ai',
  type = 'website',
  author = 'SalesGenie',
  publishedTime,
  modifiedTime,
  locale = 'en_US',
  noIndex = false,
}: SEOProps) {
  const siteName = 'SalesGenie';
  
  const pageTitle = useMemo(() => {
    if (title && title !== 'SalesGenie - AI Customer Support & Sales Automation') {
      return `${title} | ${siteName}`;
    }
    return title;
  }, [title]);

  useEffect(() => {
    const updateMeta = () => {
      document.title = pageTitle;

      let metaTitle = document.querySelector('meta[property="og:title"]');
      if (!metaTitle) {
        metaTitle = document.createElement('meta');
        metaTitle.setAttribute('property', 'og:title');
        document.head.appendChild(metaTitle);
      }
      metaTitle.setAttribute('content', pageTitle);

      let metaDescription = document.querySelector('meta[name="description"]');
      if (!metaDescription) {
        metaDescription = document.createElement('meta');
        metaDescription.setAttribute('name', 'description');
        document.head.appendChild(metaDescription);
      }
      metaDescription.setAttribute('content', description);

      let metaKeywords = document.querySelector('meta[name="keywords"]');
      if (!metaKeywords) {
        metaKeywords = document.createElement('meta');
        metaKeywords.setAttribute('name', 'keywords');
        document.head.appendChild(metaKeywords);
      }
      metaKeywords.setAttribute('content', keywords.join(', '));

      const ogTags = [
        { property: 'og:title', content: pageTitle },
        { property: 'og:description', content: description },
        { property: 'og:image', content: image },
        { property: 'og:url', content: url },
        { property: 'og:type', content: type },
        { property: 'og:site_name', content: siteName },
        { property: 'og:locale', content: locale },
      ];

      ogTags.forEach(({ property, content }) => {
        let tag = document.querySelector(`meta[property="${property}"]`);
        if (!tag) {
          tag = document.createElement('meta');
          tag.setAttribute('property', property);
          document.head.appendChild(tag);
        }
        tag.setAttribute('content', content);
      });

      const twitterTags = [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: pageTitle },
        { name: 'twitter:description', content: description },
        { name: 'twitter:image', content: image },
        { name: 'twitter:site', content: '@salesgenie' },
        { name: 'twitter:creator', content: author },
      ];

      twitterTags.forEach(({ name, content }) => {
        let tag = document.querySelector(`meta[name="${name}"]`);
        if (!tag) {
          tag = document.createElement('meta');
          tag.setAttribute('name', name);
          document.head.appendChild(tag);
        }
        tag.setAttribute('content', content);
      });

      if (publishedTime) {
        let tag = document.querySelector('meta[property="article:published_time"]');
        if (!tag) {
          tag = document.createElement('meta');
          tag.setAttribute('property', 'article:published_time');
          document.head.appendChild(tag);
        }
        tag.setAttribute('content', publishedTime);
      }

      if (modifiedTime) {
        let tag = document.querySelector('meta[property="article:modified_time"]');
        if (!tag) {
          tag = document.createElement('meta');
          tag.setAttribute('property', 'article:modified_time');
          document.head.appendChild(tag);
        }
        tag.setAttribute('content', modifiedTime);
      }

      if (type === 'article') {
        let tag = document.querySelector('meta[property="og:article:published_time"]');
        if (!tag) {
          tag = document.createElement('meta');
          tag.setAttribute('property', 'article:published_time');
          document.head.appendChild(tag);
        }
        tag.setAttribute('content', publishedTime || new Date().toISOString());
      }

      if (noIndex) {
        let noIndexTag = document.querySelector('meta[name="robots"]');
        if (!noIndexTag) {
          noIndexTag = document.createElement('meta');
          noIndexTag.setAttribute('name', 'robots');
          document.head.appendChild(noIndexTag);
        }
        noIndexTag.setAttribute('content', 'noindex, nofollow');
      }

      const structuredData = {
        '@context': 'https://schema.org',
        '@type': type === 'website' ? 'WebSite' : type === 'article' ? 'Article' : 'Product',
        name: pageTitle,
        description: description,
        url: url,
        image: image,
        author: {
          '@type': 'Person',
          name: author,
        },
      };

      if (type === 'article' && publishedTime) {
        structuredData.datePublished = publishedTime;
      }
      if (type === 'article' && modifiedTime) {
        structuredData.dateModified = modifiedTime;
      }

      let script = document.querySelector('script[type="application/ld+json"]');
      if (!script) {
        script = document.createElement('script');
        script.setAttribute('type', 'application/ld+json');
        document.head.appendChild(script);
      }
      script.textContent = JSON.stringify(structuredData);
    };

    updateMeta();

    return () => {
      const metaTags = [
        'meta[property="og:title"]',
        'meta[property="og:description"]',
        'meta[property="og:image"]',
        'meta[property="og:url"]',
        'meta[property="og:type"]',
        'meta[property="og:site_name"]',
        'meta[property="og:locale"]',
        'meta[name="description"]',
        'meta[name="keywords"]',
        'meta[name="twitter:card"]',
        'meta[name="twitter:title"]',
        'meta[name="twitter:description"]',
        'meta[name="twitter:image"]',
        'meta[name="twitter:site"]',
        'meta[name="twitter:creator"]',
        'script[type="application/ld+json"]',
      ];
      
      metaTags.forEach(selector => {
        const tag = document.querySelector(selector);
        if (tag) {
          tag.remove();
        }
      });
    };
  }, [pageTitle, description, keywords, image, url, type, author, publishedTime, modifiedTime, locale, noIndex]);

  return null;
}

export function Breadcrumbs({ 
  items, 
  separator = ' / ' 
}: { 
  items: { label: string; href?: string }[]; 
  separator?: string;
}) {
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
          <li key={index} itemProp="itemListElement" itemScope itemType="https://schema.org/ListItem">
            <span>
              {item.href ? (
                <a 
                  href={item.href} 
                  itemProp="item"
                  className="text-gray-600 hover:text-blue-600 transition-colors"
                >
                  <span itemProp="name">{item.label}</span>
                </a>
              ) : (
                <span 
                  className="text-gray-900 font-medium"
                  itemProp="name"
                  aria-current={index === items.length - 1 ? 'page' : undefined}
                >
                  {item.label}
                </span>
              )}
            </span>
            {index < items.length - 1 && (
              <span 
                className="text-gray-400" 
                aria-hidden="true"
              >
                {separator}
              </span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}

export function JsonLd({ data }: { data: Record<string, unknown> }) {
  useEffect(() => {
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.text = JSON.stringify(data);
    document.head.appendChild(script);

    return () => {
      const existingScript = document.querySelector('script[type="application/ld+json"]');
      if (existingScript) {
        existingScript.remove();
      }
    };
  }, [data]);

  return null;
}