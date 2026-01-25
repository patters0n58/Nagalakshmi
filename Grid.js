import React from 'react'
import Row from './Row'

export default function Grid({currentGuess, guesses, turn}) {
  return (
    <div>
        {guesses.map((g, i)=>{
          if (g) {

            return <Row key={i} guess={g} />
          }
            if(turn === i){
              return <Row key={i} currentGuess = {currentGuess} />
            }
            return <Row key={i} />
        })}
    </div>
  )
}
