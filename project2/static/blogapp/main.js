fetch('/api/posts/')
  .then(res => res.json())
  .then(data => {
    const postDiv = document.getElementById('posts');
    data.forEach(post => {
      postDiv.innerHTML += `
        <h3>${post.title}</h3>
        <p>${post.content}</p>
        <a href="/posts/${post.id}/">View Comments</a>
        <hr/>
      `;
    });
  });
