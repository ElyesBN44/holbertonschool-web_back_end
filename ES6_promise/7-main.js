import loadBalancer from './7-load_balancer';

const ukSuccess = 'Downloading from UK is faster';
const frSuccess = 'Downloading from FR is faster';

const promiseUK = new Promise((resolve) => {
  setTimeout(resolve, 100, ukSuccess);
});

const promiseUKSlow = new Promise((resolve) => {
  setTimeout(resolve, 400, ukSuccess);
});

const promiseFR = new Promise((resolve) => {
  setTimeout(resolve, 200, frSuccess);
});

const test = async () => {
 
  const resultUK = await loadBalancer(promiseUK, promiseFR);
  const resultUKSlow = await loadBalancer(promiseUKSlow, promiseFR);

  
  console.log(resultUK);
  console.log(resultUKSlow);
};

test();
