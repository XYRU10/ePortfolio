// Dynamically load sections
function loadSection(id, file) {
    fetch(file)
      .then(res => {
        if (!res.ok) throw new Error(`Failed to load ${file}`);
        return res.text();
      })
      .then(content => {
        document.getElementById(id).innerHTML = content;
      })
      .catch(err => console.error(err));
  }
  
  // Load each section
  loadSection('header', 'header.html');
  loadSection('home', 'home.html');
  loadSection('about', 'about.html');
  loadSection('projects', 'projects.html');
  loadSection('contact', 'contact.html');
  loadSection('footer', 'footer.html');
  