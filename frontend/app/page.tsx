"use client"; // Adicione esta linha para marcar o componente como Client Component

import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [body, setBody] = useState('');

  useEffect( () => {
    axios
      .get("http://127.0.0.1:9000/get_personagens")
      .then((response) => {
        console.log(response)
        const data = response.data
        setBody(data['body'])
      })
      .catch( (erro) => {
        //aaa
      })
  }, [])

  return (
    <div>
      <h1>{body}</h1> {/* Exibindo o valor de body */}
    </div>
  );
}
