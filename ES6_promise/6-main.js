import handleProfileSignup from './6-final-user';

async function main() {
  const result = await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');
  console.log(result);
}

main();
