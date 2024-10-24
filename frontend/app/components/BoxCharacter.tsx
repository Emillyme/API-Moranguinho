"use client"; // Para marcar o componente como Client Component
import { useEffect, useState } from 'react';
import axios from 'axios';

interface Personagem {
  id: number;
  nome: string;
  imagem: string; 
  idade: number;
  gosta: string;
  nao_gosta: string;
}

const BoxCharacter = () => {
    const [personagens, setPersonagens] = useState<Personagem[]>([]); // Definindo o tipo do estado

    useEffect(() => {
    fetch('http://localhost:9000/personagens')
        .then(response => response.json())
        .then(data => setPersonagens(data))
        .catch(error => console.error('Erro ao buscar personagens:', error));
    }, []);

    return (
        <div>
            {personagens.map(personagem => (
            <div key={personagem.id}>
                <h2>{personagem.nome}</h2>
                <img src={personagem.imagem} alt={personagem.nome} />
                <p>Idade: {personagem.idade}</p>
                <p>Gosta: {personagem.gosta}</p>
                <p>Não gosta: {personagem.nao_gosta}</p>
            </div>
            ))}
        </div>
    );
}

