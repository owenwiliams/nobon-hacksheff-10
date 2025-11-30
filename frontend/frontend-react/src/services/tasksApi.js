import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const getAllTasks = async () => {
  const response = await axios.get(`${BASE_URL}/tasks/`);
  return response.data;
};

export const getTask = async (id) => {
  const response = await axios.get(`${BASE_URL}/tasks/${id}`);
  return response.data;
};

export const createTask = async (taskData) => {
  const response = await axios.post(`${BASE_URL}/tasks/`, taskData);
  return response.data;
};

export const updateTask = async (id, taskData) => {
  const response = await axios.put(`${BASE_URL}/tasks/${id}`, taskData);
  return response.data;
};

export const deleteTask = async (id) => {
  const response = await axios.delete(`${BASE_URL}/tasks/${id}`);
  return response.data;
};