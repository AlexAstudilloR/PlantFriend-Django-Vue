<template>
    <div class="landing-page">
      <!-- Sección de Introducción -->
      <section class="hero">
        <h1>Bienvenido a PlantFriends</h1>
        <p>Tu guía personalizada para el cuidado de plantas y jardinería en casa.</p>
        <router-link to="/register" class="cta-button">Únete Ahora</router-link>
      </section>
  
      <!-- Sección Quiénes Somos -->
      <section class="about-us">
        <h2>¿Quiénes Somos?</h2>
        <p>
          En <strong>PlantFriends</strong>, creemos que cualquiera puede convertirse en un jardinero exitoso con un poco de ayuda. 
          Nuestra plataforma está diseñada para todos los amantes de las plantas, desde principiantes hasta expertos, 
          que desean crear y mantener un jardín casero vibrante y saludable.
        </p>
        <p>
          Nuestra misión es brindarte una guía completa y personalizada sobre los cuidados necesarios para cada planta. 
          Ya sea que quieras cultivar hierbas aromáticas, flores exóticas, o vegetales frescos, 
          te ofrecemos recomendaciones detalladas y consejos prácticos para asegurar que tus plantas florezcan y prosperen.
        </p>
      </section>
  
      <!-- Sección de Comunidad -->
      <section class="community">
        <h2>Únete a Nuestra Comunidad Verde</h2>
        <p>
          En <strong>PlantFriends</strong>, no solo obtienes información; también formas parte de una comunidad apasionada 
          por la naturaleza. Aprende de otros jardineros, comparte tus logros, y descubre las mejores prácticas 
          para cada etapa de crecimiento de tus plantas.
        </p>
      </section>
  
      <!-- Sección de Registro -->
      <section class="call-to-action">
        <h2>¿Listo para Empezar?</h2>
        <p>Transforma tu hogar en un oasis verde con PlantFriends.</p>
        <router-link to="/login" class="cta-button">Empecemos</router-link>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "LandingPage",
  };
  </script>
  
  <style scoped>
  .landing-page {
    text-align: center;
    padding: 2rem;
    min-height: 100vh;
    
  }
  
  .hero {
    padding: 2rem;
    background-color: #eaf6ea;
  }
  
  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .hero p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
  }
  
  .about-us, .community, .call-to-action {
    margin-top: 2rem;
    padding: 2rem;
  }
  
  h2 {
    font-size: 2rem;
    color: #4CAF50;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.125rem;
    color: #555;
    line-height: 1.5;
  }
  
  .cta-button {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.75rem 1.5rem;
    background-color: #4CAF50;
    color: #fff;
    border-radius: 5px;
    text-decoration: none;
    font-size: 1rem;
  }
  
  .cta-button:hover {
    background-color: #45a049;
  }
  </style>
  