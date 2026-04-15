<template>
  <q-page class="about-page">

    <!-- 🔥 HERO -->
    <div class="hero">
      <div class="overlay">
        <h1>About Parallel</h1>
        <p>A Division of Pushpa Textile</p>
      </div>
    </div>

    <!--  STORY -->
    <div class="container grid">
      <div class="img-wrapper">
        <img :src="storyImg" />
      </div>

      <div class="story-text">
        <h2>Our Story</h2>
        <p>
          Founded in Solapur, Pushpa Textile started with traditional power looms.
          Over time, it evolved into a trusted manufacturer serving hospitals,
          industries, and institutions across India.
        </p>
        <p>
          With innovation, quality, and commitment, Parallel continues to redefine
          textile excellence.
        </p>
      </div>
    </div>

    <!-- 👥 TEAM -->
    <div class="container">
      <h2 class="section-title">Our Leadership</h2>

      <div class="team-grid">
        <div class="team-card" v-for="(m,i) in team" :key="i">
          <div class="team-img-wrapper">
            <img :src="m.img" />
          </div>

          <h3>{{ m.name }}</h3>
          <p class="desc">{{ m.desc }}</p>
        </div>
      </div>
    </div>

  </q-page>
</template>

<script>
import storyImg from '../assets/About/story.png'
import pankaj from '../assets/About/pankaj.png'
import prashant from '../assets/About/prashant.png'
import sapna from '../assets/About/sapna.png'
import suresh from '../assets/About/sureshchandra.png'

export default {
  data() {
    return {
      storyImg,
      team: [
        {
          name: "Sureshchandra Rathi",
          img: suresh,
          desc: "The Person who laid the first Bricks of Pushpa Textile. Starting with power looms and the manufacturing of the Solapur Chaddar. His hard work, dedication and vision has brought growth and expansion over the years."
        },
        {
          name: "Prashant Rathi",
          img: prashant,
          desc: "He started the Garment division of our firm. And built a Brand around Pushpa Textile and those associated with it. With his zeal and enthusiasm, he ensure quality and timely delivery. He studied at Symbiosis Pune and did his MBA at Sydney."
        },
        {
          name: "Sapna Rathi",
          img: sapna,
          desc: "She brings her expertise in to execute on the ground operations and create sustainable processes in house for our Garment Unit. She is an MBA graduate from Pune with experience working with IT companies for ISO Processes."
        },
        {
          name: "Pankaj Rathi",
          img: pankaj,
          desc: "He manages our Overseas Operations. He graduated from VJTI Mumbai as Gold Medalist in Textile Engineering & completed Masters degree in Textiles & Supply Chain from Cornell University, NY. Currently based in Houstan Texas and leading a Global Shipping Business."
        }
      ]
    }
  }
}
</script>

<style scoped>

.about-page {
  background: #f8fafc;
}

/* 🔥 HERO */
.hero {
  height: 260px;
  background: linear-gradient(135deg, #0f2027, #2c5364);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
}

.overlay h1 {
  font-size: 38px;
  font-weight: bold;
}

.overlay p {
  opacity: 0.85;
}

/* 📦 CONTAINER */
.container {
  max-width: 1100px;
  margin: 60px auto;
  padding: 0 20px;
}

/* 🧵 STORY GRID */
.grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 40px;
  align-items: center;
}

/* 🔥 STORY IMAGE FIX (HEIGHT CONTROLLED) */
.img-wrapper {
  width: 100%;
  height: 220px; /* ✅ reduced height */
  overflow: hidden;
  border-radius: 16px;
}

.img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* TEXT */
.story-text h2 {
  font-size: 26px;
  margin-bottom: 10px;
}

.story-text p {
  color: #555;
  line-height: 1.6;
}

/* 👥 TEAM */
.section-title {
  text-align: center;
  font-size: 26px;
  margin-bottom: 30px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 25px;
}

/* 🔥 CARD */
.team-card {
  background: white;
  padding: 18px;
  border-radius: 16px;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(0,0,0,0.06);
}

.team-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.1);
}

/* 🔥 IMAGE FIX (NO STRETCH) */
.team-img-wrapper {
  width: 100%;
  height: 230px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border-radius: 14px;
  overflow: hidden;
}

.team-img-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  transition: 0.4s;
}

/* HOVER ZOOM */
.team-card:hover img {
  transform: scale(1.05);
}

/* TEXT */
.team-card h3 {
  margin-top: 14px;
  font-size: 18px;
  line-height: 1.3;
}

.desc {
  font-size: 13px;
  color: #666;
  margin-top: 6px;
}

/* 📱 RESPONSIVE */
@media (max-width: 900px) {
  .grid {
    grid-template-columns: 1fr;
  }

  .team-grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 500px) {
  .team-grid {
    grid-template-columns: 1fr;
  }
}

</style>