/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e0f7ff',
          100: '#b3ebff',
          200: '#80deff',
          300: '#4dd1ff',
          400: '#1fc4ff',
          500: '#009edb',
          600: '#008ec5',
          700: '#0075a4',
          800: '#005c82',
          900: '#003f57',
        },
        // gold: '#f5c242',
        charcoal: '#1f2933'
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' }
        }
      },
      animation: {
        marquee: 'marquee 15s linear infinite'
      }
    }
  },
  plugins: [],
}
