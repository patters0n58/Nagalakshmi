import React from 'react'

export default function Modal({isCorrect, turn, solution}) {
  return (
    <div className = "modal">
    console.log({isCorrect})
     {isCorrect && (
        <div>
            <h1>You 've won !</h1>
            <p className = "solution">{solution} </p>
            <p> You found it in {turn} guesses</p>
        </div>
     )}
     {isCorrect && (
        <div>
            <h1>You lost !</h1>
            <p className = "solution">{solution} </p>
            <p> Better luck next time</p>
        </div>
     )}
        
   </div>
  )
}
