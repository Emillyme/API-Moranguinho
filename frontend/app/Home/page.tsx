"use client";
import Image from 'next/image';

export default function Home() {
  return (
    <>
      <div className="container mx-auto p-4">
        <header className='flex justify-between items-center'>
          <Image
            src='/images/moranguin.png'
            alt="Moranguin"
            width={600} 
            height={300}
          />
          <li className='flex flex-col items-center'>
            <Image
              src='/images/logo.png'
              alt='logo'
              width={650} 
              height={0}
              className='mb-10'
            />
            <h1 className='p-[10px] px-[70px] text-2xl text-center bg-pink text-white bold'>API</h1>
          </li>
        </header>
      </div>
    </>
  );
}
