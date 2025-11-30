import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const getAllEntries = async () => {
  const response = await axios.get(`${BASE_URL}/entries/`);
  return response.data;
};

export const getEntry = async (id) => {
  const response = await axios.get(`${BASE_URL}/entries/${id}`);
  return response.data;
};

export const createEntry = async (entryData) => {
  const response = await axios.post(`${BASE_URL}/entries/`, entryData);
  return response.data;
};

export const updateEntry = async (id, entryData) => {
  const response = await axios.put(`${BASE_URL}/entries/${id}`, entryData);
  return response.data;
};

export const deleteEntry = async (id) => {
  const response = await axios.delete(`${BASE_URL}/entries/${id}`);
  return response.data;
};