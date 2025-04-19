/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './layouts/**/*.html', 
    './content/**/*.md', 
    './content/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        'retro-background': '#0a0f0a', // Darker green-tinted black
        'retro-foreground': '#00e300', // CRT green
        'retro-accent': '#33ff33',     // Brighter green accent
      },
      boxShadow: {
        'retro-glow': '0 0 3px rgba(51, 255, 51, 0.3)', // CRT glow
        'retro-glow-lg': '0 0 5px rgba(51, 255, 51, 0.3)', // Brighter glow for headers/links
      },
      fontFamily: {
        'mono': ['JetBrains Mono', 'Fira Code', 'SF Mono', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace'],
      },
      // Enhanced typography config
      typography: ({ theme }) => ({
        invert: {
          css: {
            '--tw-prose-body': theme('colors.retro-foreground'),
            '--tw-prose-headings': theme('colors.retro-accent'),
            '--tw-prose-lead': theme('colors.retro-accent'),
            '--tw-prose-links': theme('colors.retro-accent'),
            '--tw-prose-bold': theme('colors.retro-foreground'),
            '--tw-prose-counters': theme('colors.retro-foreground'),
            '--tw-prose-bullets': theme('colors.retro-accent'),
            '--tw-prose-hr': theme('colors.retro-accent / 0.3'),
            '--tw-prose-quotes': theme('colors.retro-foreground'),
            '--tw-prose-quote-borders': theme('colors.retro-accent / 0.5'),
            '--tw-prose-captions': theme('colors.retro-foreground / 0.9'),
            '--tw-prose-code': theme('colors.retro-accent'),
            '--tw-prose-pre-bg': 'rgba(10, 15, 10, 0.8)',
            '--tw-prose-pre-code': theme('colors.retro-foreground'),
            '--tw-prose-th-borders': theme('colors.retro-accent / 0.3'),
            '--tw-prose-td-borders': theme('colors.retro-accent / 0.2'),
            
            // Font styles
            h1: {
              fontWeight: '700',
              marginTop: '2em',
              marginBottom: '1em',
              letterSpacing: '0.05em',
            },
            h2: {
              fontWeight: '700',
              marginTop: '1.75em',
              marginBottom: '0.75em',
              letterSpacing: '0.05em',
            },
            a: {
              textDecoration: 'none',
              fontWeight: '500',
              '&:hover': {
                color: theme('colors.retro-background'),
                backgroundColor: theme('colors.retro-accent'),
                borderRadius: '0.125rem',
              },
            },
            pre: {
              backgroundColor: 'rgba(10, 15, 10, 0.8)',
              borderWidth: '1px',
              borderColor: theme('colors.retro-accent / 0.3'),
              borderRadius: '0.25rem',
              padding: theme('spacing.4'),
              boxShadow: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.2)',
            },
            code: {
              backgroundColor: 'rgba(10, 15, 10, 0.8)',
              borderWidth: '1px',
              borderColor: theme('colors.retro-accent / 0.3'),
              borderRadius: '0.125rem',
              padding: '0.125rem 0.25rem',
              fontWeight: '400',
            },
            'code::before': {
              content: '""',
            },
            'code::after': {
              content: '""',
            },
            blockquote: {
              fontStyle: 'normal',
              fontWeight: '400',
              borderLeftWidth: '2px',
              borderLeftColor: theme('colors.retro-accent / 0.5'),
              paddingLeft: '1em',
              fontFamily: theme('fontFamily.mono'),
            },
            // Add more custom styling as needed
          },
        },
      }),
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
} 