import http from 'k6/http';

export const options = {
    vus: 50,
    duration: '60s',
};

export default function () {
    http.get(`${__ENV.TARGET_URL}/health`);
}