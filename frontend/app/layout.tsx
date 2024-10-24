import type { Metadata } from "next";
import { Poppins } from 'next/font/google';
import "./globals.css";

const poppins = Poppins({
  weight: ['400', '700'], // Escolha os pesos que deseja utilizar
  subsets: ['latin'],     // Escolha os subsets
});

export const metadata: Metadata = {
  title: "Moranguinho API",
  description: "API da moranguinho, com os personagens e com CRUD.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${poppins.className} antialiased`}>
        {children}
      </body>
    </html>
  );
}
