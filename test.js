import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp-up to 100 users
    { duration: '5m', target: 100 }, // Stay at 100 users
    { duration: '2m', target: 0 },   // Ramp-down
  ],
};

export default function () {
  let res = http.get('http://10.96.224.187:8080/price?product_id=P124');
  check(res, { 'status was 200': (r) => r.status === 200 });
  sleep(1);
}

