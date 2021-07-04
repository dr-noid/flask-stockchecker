module.exports = {
  mode: 'jit',
  purge: [
    './app/templates/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'darkgray': '#1E1E1E',
        'textwhite': '#FFFFFF',
        'lightblue': '#9CDCFE',
        'lightyellow': '#FEE082',
        'lavender': '#9046FE',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
