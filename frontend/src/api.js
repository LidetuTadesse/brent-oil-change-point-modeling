// File: frontend/src/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000/api', // adjust if your Flask is hosted differently
});

export const fetchLogReturns = () => API.get('/log_returns');
export const fetchChangePoints = () => API.get('/change_points');
export const fetchEvents = () => API.get('/events');
