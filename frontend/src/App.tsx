import { useState } from 'react'
import { createShortURL, getURL, updateShortURL, deleteURL, getStats } from './api/api'
import { URLCreate, URLResponse, URLUpdate } from './api/types'

export default function App() {


  return (
    <>
      <main>
        
        <section>
          <p>Shorten a long URL</p>
          <input placeholder="Enter long link here"></input>
          <button>Shorten URL</button>
        </section>
        
        <section>
          <p>Shortend URL Link</p>
          <p></p>
        </section>
        
      </main>
    </>
  )
}