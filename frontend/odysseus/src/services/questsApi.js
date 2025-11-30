import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const getAllQuests = async () => {
  const response = await axios.get(`${BASE_URL}/quests/`);
  return response.data;
};

export const getQuest = async (id) => {
  const response = await axios.get(`${BASE_URL}/quests/${id}`);
  return response.data;
};

export const getQuestsByEndDate = async (endDate) => {
  try {
    const res = await axios.get(`${BASE_URL}/quests/by-end-date/${endDate}`);
    return res.data;
  } catch (err) {
    console.error("Error fetching quests by end date:", err);
    return [];
  }
};

export const getActiveQuests = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/quests/active`);
    return res.data;
  } catch (err) {
    console.error("Error fetching active quests:", err);
    return [];
  }
};

export const getTasksByQuest = async (questId) => {
  try {
    const res = await axios.get(`${BASE_URL}/quests/tasks/${questId}`);
    return res.data;
  } catch (err) {
    console.error("Error fetching tasks:", err);
    return [];
  }
};

export const createQuest = async (questData) => {
  const response = await axios.post(`${BASE_URL}/quests/`, questData);
  return response.data;
};

export const updateQuest = async (id, questData) => {
  const response = await axios.put(`${BASE_URL}/quests/${id}`, questData);
  return response.data;
};

export const deleteQuest = async (id) => {
  const response = await axios.delete(`${BASE_URL}/quests/${id}`);
  return response.data;
};