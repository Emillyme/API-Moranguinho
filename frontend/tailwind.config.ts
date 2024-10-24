import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        pink: "var(--pink-strawberry)",
        red: "var(--red-strawberry)",
        blue: "var(--blue-strawberry)",
        purple: "var(--purple-strawberry)",
        brown: "var(--text-strawberry)",
      },
    },
  },
  plugins: [],
};

export default config;
