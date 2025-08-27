import { useState } from 'react'
import { createShortURL, getURL, updateShortURL, deleteURL, getStats } from './api/api'
import type { URLCreate, URLResponse, URLUpdate } from './api/types'

export default function App() {
  const [longURL, setLongURL] = useState("")
  const [shortened, setShortened] = useState<URLResponse | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleShorten = async() => {
    if (!longURL.trim()) {
      setError("Please enter a valid URL.")
      return
    }

    try {
      const response = await createShortURL({ url: longURL })
      setShortened(response.data)
      setError(null)
    } catch (err) {
      setError("Failed to shorten the URL. Try again.")
    }
  }

  return (
    <>
      <main className='p-6'>
        
        <section className='mb-6'>
          <p className='font-semibold'>Shorten a long URL</p>
          <input 
            value={ longURL }
            onChange={ (e) => setLongURL(e.target.value) }
            placeholder="Enter long link here"
            className='border p-2 rounded mr-2 w-80'
          ></input>
          <button
            onClick={handleShorten}
            className='bg-blue-500 text-white px-4 py-2 rounded'
          >Shorten URL</button>
          { error && <p className='text-red-500 mt-2'>{ error }</p>}
        </section>
        
        { shortened && (
          <section>
            <p className='font-semibold'>Shortend URL Link</p>
            <a 
              href={`http://localhost:8000/${shortened.shortCode}`}
              target='_blank'
              rel='noopener noreferrer'
              className='text-blue-600 underline'
            >{`http://localhost:8000/${shortened.shortCode}`}</a>
            <p className='mt-2 text-sm text-gray-600'>
              Accessed { shortened.accessCount } times
            </p>
          </section>
        )}
        
      </main>
    </>
  )
}