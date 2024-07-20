/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html, jinja}"],
    theme: {
        colors: {
            transparent: "transparent",
            white: "#ffffff",
            verde: "#38c7c7",
            aqua: "#389AC7",
            aqualight: "#6acbf7",
            blue: "#2B363F",
            green: "#38C796"
        },
        container: {
            center: true,
            padding: {
                DEFAULT: '1rem',
                sm: '2rem',
                lg: '4rem',
                xl: '5rem',
                '2xl': '6rem',
            },
        }
    },
    plugins: [],
}

