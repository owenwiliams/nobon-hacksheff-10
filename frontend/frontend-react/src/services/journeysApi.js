import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const getAllJourneys = async () => {
  const response = await axios.get(`${BASE_URL}/journey/`);
  return response.data;
};

export const getJourney = async (id) => {
  const response = await axios.get(`${BASE_URL}/journey/${id}`);
  return response.data;
};

export const getQuestsByJourney = async (journeyId) => {
  try {
    const res = await axios.get(`${BASE_URL}/quests/${journeyId}`);
    return res.data;
  } catch (err) {
    console.error("Error fetching quests:", err);
    return [];
  }
};

export const getJourneysByEndDate = async (endDate) => {
  try {
    const res = await axios.get(`${BASE_URL}/by-end-date/${endDate}`);
    return res.data;
  } catch (err) {
    console.error("Error fetching journeys by end date:", err);
    return [];
  }
};

export const getActiveJourneys = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/active`);
    return res.data;
  } catch (err) {
    console.error("Error fetching active journeys:", err);
    return [];
  }
};

export const createJourney = async (journeyData) => {
  const response = await axios.post(`${BASE_URL}/journey/`, journeyData);
  return response.data;
};

export const updateJourney = async (id, journeyData) => {
  const response = await axios.put(`${BASE_URL}/journey/${id}`, journeyData);
  return response.data;
};

export const deleteJourney = async (id) => {
  const response = await axios.delete(`${BASE_URL}/journey/${id}`);
  return response.data;
};