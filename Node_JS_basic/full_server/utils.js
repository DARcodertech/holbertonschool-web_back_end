import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.trim().split('\n');
        const header = lines.shift().split(',');
        const studentByField = {};

        for (const line of lines) {
          const student = line.split(',');
          const field = student[3];
          const firstName = student[0];

          if (!studentByField[field]) {
            studentByField[field] = [];
          }
          studentByField[field].push(firstName);
        }

        resolve(studentByField);
      }
    });
  });
}
