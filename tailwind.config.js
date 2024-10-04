/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html', './*.html'],
  theme: {
    colors: {
      'white': '#ffffff',
      'gray-dark': '#0f172a',
      'gray': '#334155',
      'gray-light': '#94a3b8',
      'purple-dark': '#312e81',
      'purple': '#4338ca',
      'purple-light': '#818cf8'
    },
    fontFamily: {
      sans: ['Ubuntu', 'sans-serif'],
    },
    extend: {
      spacing: {
        '8xl': '96rem',
        '9xl': '128rem',
      },
      borderRadius: {
        '4xl': '2rem',
      }
    }
  },
}