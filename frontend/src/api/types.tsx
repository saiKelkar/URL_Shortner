export type URLCreate = {
    url: string;
}

export type URLResponse = URLCreate & {
    id: number;
    shortCode: string;
    createdAt?: string;
    updatedAt?: string;
    accessCount: number;
}

export type URLUpdate = {
    shortCode: string;
}