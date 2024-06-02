curl -g http://127.0.0.1:5000/api/winners?where={%22country%22:%22France%22}
curl -g http://127.0.0.1:5000/api/winners?where={%22year%22:{%20%22$gt%22:2000},%22gender%22:%22female%22}