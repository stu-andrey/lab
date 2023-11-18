const WORKS_URL = "http://localhost:8000/"
const WORKS_IMAGES_URL = WORKS_URL + "static/images/works/";
const WORKS_API = WORKS_URL + "api/works";

const checkReponse = (res) => {
  return res.ok ? res.json() : res.json().then((err) => Promise.reject(err));
};

const getWorks = () => fetch(`${WORKS_API}`).then(checkReponse);

const getWorkById = (id) => fetch(`${WORKS_API}/id/${id}`).then(checkReponse);

export {
    WORKS_URL, WORKS_IMAGES_URL, WORKS_API, 
    getWorks, getWorkById
}