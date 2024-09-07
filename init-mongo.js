db.createUser({
    user: 'shorter',
    pwd: 'strongpassforshorter',
    roles: [{ role: 'readWrite', db: 'urlshortener' }],
  });

db = new Mongo().getDB('urlshortener');