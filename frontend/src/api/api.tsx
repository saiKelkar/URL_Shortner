import axios from "axios";
import type { URLCreate, URLResponse, URLUpdate } from "./types";

const API = axios.create({
    baseURL: "http://localhost:8000",
});

export const createShortURL = (url: URLCreate) => 
    API.post<URLResponse>("/shorten/", url);

export const getURL = (shortCode: string) =>
    API.get<URLResponse>(`/shorten/${shortCode}`);

export const updateShortURL = (id: number, url_update: URLUpdate) => 
    API.put<URLResponse>(`/shorten/${id}`, url_update)

export const deleteURL = (id: number) => 
    API.delete<{ message: string }>(`/shorten/${id}`);

export const getStats = (id: number) => 
    API.get<URLResponse>(`/shorten/${id}/stats`)