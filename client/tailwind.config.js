module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'parchment': '#cf9e5e',
        'parchment-dark': '#cb9043',
        'primary': '#000000',
        'secondary': '#cf9e5e',
        'accent': '#6B21A8', // purple-800
        'accent-dark': '#581C87',  // purple-900
      }
    },
  },
  plugins: [],
}
