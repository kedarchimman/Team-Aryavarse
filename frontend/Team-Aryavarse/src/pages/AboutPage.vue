<template>
  <q-page class="about-page">
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <h1>PARALLEL</h1>
        <p class="hero-kicker">A Division of Pushpa Textile</p>
        <p class="hero-subtitle">
          Built on legacy, refined through quality, and designed for modern professional wear.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container story-grid">
        <div class="story-image-card">
          <img
            src="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=1200&q=80"
            alt="Textile legacy"
          />
        </div>

        <div class="story-content">
          <p class="section-label">OUR STORY</p>
          <h2>One of the pioneers of Solapur textile industry..</h2>

          <p>
            Incorporated in the year 1975, the first brick of “Pushpa Textile” was laid by Shri Sureshchandra Ramkisan Rathi at Solapur, Maharashtra India under the chairmanship of Shri Ramkisan Rathi.
            It started with 12 looms, Pushpa Textile operates a complete in-house manufacturing unit of Jacquard Design Solapuri Chaddars and Turkish Towels.
          </p>

          <p>
            Since then company has made rapid progress having 200 looms at 5 processing units today. Now, we have grown to a brand for the apparel industry, Hotel and Hospital Linen Range, Corporate and School Uniforms, Jute Bags, Printed Bedsheets and so much more. All this made at our new factory with new age machinery to be the textile company you trust and love using.
            At Pushpa Textile, we always look forward maintaining quality and honoring its commitments..
          </p>

          <p>
            Parallel
            A Division of Pushpa Textile
            Today, Parallel carries this same foundation forward with a more
            contemporary approach. It combines years of manufacturing experience
            with modern design thinking to create apparel that is functional,
            durable, and professionally refined.
          </p>
        </div>
      </div>
    </section>

    <section class="section light-section">
      <div class="container">
        <div class="section-heading center">
          <p class="section-label">50 YEARS OF TEXTILE EXCELLENCE</p>
          <h2>Manufacturing strength with premium presentation.</h2>
          <p class="section-intro">
            Our process is built on quality control, structured production,
            precision finishing, and a deep understanding of textile performance.
          </p>
        </div>

        <div class="feature-grid">
          <div class="feature-card">
            <div class="feature-icon">01</div>
            <h3>Quality First</h3>
            <p>
              Every stage of production is guided by consistency, attention to
              detail, and dependable finishing standards.
            </p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">02</div>
            <h3>Modern Production</h3>
            <p>
              We combine manufacturing discipline with updated processes to
              deliver apparel that meets present-day professional needs.
            </p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">03</div>
            <h3>Functional Design</h3>
            <p>
              Our products are developed with comfort, durability, and practical
              usability in mind for modern work environments.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="section soft-section">
      <div class="container values-grid">
        <div class="value-card">
          <p class="section-label">OUR PLEDGE</p>
          <h3>Trusted quality in every product.</h3>
          <p>
            We are committed to delivering products that reflect quality India Textile,
            consistency, and professional reliability in both design and finish.
          </p>
        </div>

        <div class="value-card">
          <p class="section-label">OUR MISSION</p>
          <h3>To build modern apparel with strong textile roots.</h3>
          <p>
            Our mission is to combine legacy manufacturing strength with
            innovation, comfort, and refined product development for evolving
            professional industries.
          </p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container section-heading">
        <p class="section-label">MANAGEMENT</p>
        <h2>Our Management</h2>
        <p class="section-intro leadership-intro">
          The strength of Parallel lies in the people who continue to guide the
          brand with vision, discipline, and long-term commitment to excellence.
        </p>
      </div>

      <div class="container leadership-grid">
  <div class="leader-card" v-for="member in team" :key="member.name">

    <div class="leader-image-wrap">
      <img :src="member.image" class="leader-image" />
    </div>

    <div class="leader-body">
      <h4>{{ member.name }}</h4>
      <p class="leader-role">{{ member.role }}</p>
      <p class="leader-desc">{{ member.desc }}</p>
    </div>

  </div>
</div>

    </section>
  </q-page>
</template>

<script setup>
import { aboutImg } from 'src/data/imageHelper'

const team = [
  {
    name: 'Sureshchandra Rathi',
    role: 'Founder',
    image: aboutImg('sureshchandra.png'),
    desc: 'The Person who laid the first Bricks of Pushpa Textile. Starting with power looms and the manufacturing of the Solapur Chaddar. His hard work, dedication and vision has brought growth and expansion over the years.'
  },
  {
    name: 'Prashant Rathi',
    role: 'Director',
    image: aboutImg('prashant.png'),
    desc: 'He started the Garment division of our firm. And built a Brand around Pushpa Textile and those associated with it. With his zeal and enthusiasm, he ensure quality and timely delivery. He studied at Symbiosis Pune and did his MBA at Sydney.'
  },
  {
    name: 'Sapna Rathi',
    role: 'Operations',
    image: aboutImg('sapna.png'),
    desc: 'She brings her expertise in to execute on the ground operations and create sustainable processes in house for our Garment Unit. She is an MBA graduate from Pune with experience working with IT companies for ISO Processes.'
  },
  {
    name: 'Pankaj Rathi',
    role: 'Management',
    image: aboutImg('pankaj.png'),
    desc: 'He manages our Overseas Operations. He graduated from VJTI Mumbai as Gold Medalist in Textile Engineering & completed Masters degree in Textiles & Supply Chain from Cornell University, NY. Currently based in Houstan Texas and leading a Global Shipping Business.'
  }
]
</script>

<style lang="scss">
@import 'src/css/about.scss';
</style>