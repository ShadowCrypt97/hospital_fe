<template>
  <div id="app" class="app">
    <body>
      <header class="header-area header-sticky wow slideInDown" data-wow-duration="0.75s" data-wow-delay="0s">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <nav class="main-nav">
                <!-- ***** Logo Start ***** -->
                <a href="index.html" class="logo">
                  <h4>Syntax Hospital <img src="./assets/images/logo-icon.png" alt=""></h4>
                </a>
                <!-- ***** Logo End ***** -->
                <!-- ***** Menu Start ***** -->
                <ul class="nav">
                  <li class="scroll-to-section"><a href="#top" class="active">Home</a></li>
                  <li class="scroll-to-section"><a href="#features">Features</a></li>
                  <li class="scroll-to-section"><a href="#about">About Us</a></li>
                  <li class="scroll-to-section"><a href="#services">Services</a></li>
                  <li class="scroll-to-section"><a href="#portfolio">Portfolio</a></li>
                  <li class="scroll-to-section"><a href="#contact">Contact Us</a></li>
                  <li class="scroll-to-section">
                    <div class="main-blue-button"><a href="#contact">Get Your Quote</a></div>
                  </li>
                </ul>
                <a class='menu-trigger'>
                  <span>Menu</span>
                </a>
                <!-- ***** Menu End ***** -->
              </nav>
            </div>
          </div>
        </div>
      </header>
      <main class="main-component">
        <router-view v-on:completedLogIn="completedLogIn" v-on:completedSignUp="completedSignUp">
        </router-view>
      </main>
      <footer>
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <p>Copyright © 2021 SEO Dream Co., Ltd. All Rights Reserved. 
              
              <br>Web Designed by <a rel="nofollow" href="https://templatemo.com" title="free CSS templates">TemplateMo</a></p>
            </div>
          </div>
        </div>
      </footer>
    </body>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false
    }
  },
  components: {},
  methods: {
    verifyAuth: function () {
      if (this.is_auth == false)
        this.$router.push({
          name: "logIn"
        })
    },
    loadLogIn: function () {
      this.$router.push({
        name: "logIn"
      })
    },
    loadSignUp: function () {
      this.$router.push({
        name: "signUp"
      })
    },
    completedLogIn: function (data) { },
    completedSignUp: function (data) { },
  },
  created: function () {
    this.verifyAuth()
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700;800&display=swap');
/* 
---------------------------------------------
reset
--------------------------------------------- 
*/
html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,div pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,font,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,figure,header,nav,section,article,aside,footer,figcaption {
  margin: 0;
  padding: 0;
  border: 0;
  outline: 0;
}

/* clear fix */
.grid:after {
  content: '';
  display: block;
  clear: both;
}

/* ---- .grid-item ---- */

.grid-sizer,
.grid-item {
  width: 50%;
}

.grid-item {
  float: left;
}

.grid-item img {
  display: block;
  max-width: 100%;
}

.clearfix:after {
  content: ".";
  display: block;
  clear: both;
  visibility: hidden;
  line-height: 0;
  height: 0;
}

.clearfix {
  display: inline-block;
}

html[xmlns] .clearfix {
  display: block;
}

* html .clearfix {
  height: 1%;
}

ul,
li {
  padding: 0;
  margin: 0;
  list-style: none;
}

header,
nav,
section,
article,
aside,
footer,
hgroup {
  display: block;
}

* {
  box-sizing: border-box;
}

html,
body {
  font-family: 'Open Sans', sans-serif;
  font-weight: 400;
  background-color: #fff;
  -ms-text-size-adjust: 100%;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  text-decoration: none !important;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  margin-top: 0px;
  margin-bottom: 0px;
}

ul {
  margin-bottom: 0px;
}

p {
  font-size: 15px;
  line-height: 30px;
  color: #2a2a2a;
}

img {
  width: 100%;
  overflow: hidden;
}

/* 
---------------------------------------------
global styles
--------------------------------------------- 
*/
html,
body {
  background: #fff;
  font-family: 'Open Sans', sans-serif;
}

::selection {
  background: #03a4ed;
  color: #fff;
}

::-moz-selection {
  background: #03a4ed;
  color: #fff;
}

@media (max-width: 991px) {

  html,
  body {
    overflow-x: hidden;
  }

  .mobile-top-fix {
    margin-top: 30px;
    margin-bottom: 0px;
  }

  .mobile-bottom-fix {
    margin-bottom: 30px;
  }

  .mobile-bottom-fix-big {
    margin-bottom: 60px;
  }
}

.page-section {
  margin-top: 120px;
}

.section-heading {
  margin-bottom: 60px;
}

.section-heading h6 {
  font-size: 15px;
  font-weight: 700;
  color: #33ccc5;
  text-transform: uppercase;
  margin-bottom: 15px;

}

.section-heading h2 {
  font-size: 30px;
  text-transform: capitalize;
  color: #2a2a2a;
  font-weight: 800;
  position: relative;
  z-index: 2;
  line-height: 45px;
}

.section-heading h2 em {
  font-style: normal;
  color: #33ccc5;
}

.section-heading h2 span {
  color: #088ec3;
}

.main-blue-button a {
  display: inline-block;
  background-color: #4771cb;
  font-size: 15px;
  font-weight: 400;
  color: #fff;
  text-transform: capitalize;
  padding: 12px 25px;
  border-radius: 23px;
  letter-spacing: 0.25px;
  border-bottom: 2px solid #fff !important;
  transition: all .3s;
}

.main-blue-button a:hover {
  background-color: #fff !important;
  color: #4771cb !important;
  border-bottom: 2px solid #4771cb !important;
}

.main-green-button a {
  display: inline-block;
  background-color: #33ccc5;
  font-size: 15px;
  font-weight: 400;
  color: #fff;
  text-transform: capitalize;
  padding: 12px 25px;
  border-radius: 23px;
  letter-spacing: 0.25px;
  border-bottom: 2px solid #4771cb !important;
  transition: all .3s;
}

.main-green-button a:hover {
  background-color: #4771cb !important;
  color: #fff !important;
  border-bottom: 2px solid #33ccc5 !important;
}

/* 
---------------------------------------------
header
--------------------------------------------- 
*/

.background-header {
  background-color: #33ccc5 !important;
  height: 80px !important;
  position: fixed !important;
  top: 0px;
  left: 0px;
  right: 0px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.15) !important;
}

.background-header .logo,
.background-header .main-nav .nav li a {
  color: #fff;
}

.background-header .main-nav .nav li:hover a {
  color: #33ccc5;
}

.background-header .nav li a.active {
  position: relative;
  color: #fff;
}

.background-header .nav li a.active:after {
  position: absolute;
  width: 20px;
  height: 2px;
  background-color: #4771cb;
  content: '';
  left: 50%;
  bottom: 0px;
  transform: translateX(-10px);
}

.header-area {
  background-color: #33ccc5;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  z-index: 100;
  height: 100px;
  -webkit-transition: all .5s ease 0s;
  -moz-transition: all .5s ease 0s;
  -o-transition: all .5s ease 0s;
  transition: all .5s ease 0s;
}

.header-area .main-nav {
  min-height: 80px;
  background: transparent;
}

.header-area .main-nav .logo {
  float: left;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
}

.header-area .main-nav .logo h4 {
  font-size: 30px;
  font-weight: 800;
  text-transform: capitalize;
  color: #fff;
  line-height: 100px;
  float: left;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
}

.header-area .main-nav .logo h4 img {
  max-width: 30px;
  margin-top: -20px;
  margin-left: 5px;
}

.background-header .main-nav .logo h4 {
  line-height: 80px;
}

.background-header .main-nav .nav {
  margin-top: 20px !important;
}

.header-area .main-nav .nav {
  float: right;
  margin-top: 30px;
  margin-right: 0px;
  background-color: transparent;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
  position: relative;
  z-index: 999;
}

.header-area .main-nav .nav li {
  padding-left: 20px;
  padding-right: 20px;
}

.header-area .main-nav .nav li:last-child {
  padding-right: 0px;
  padding-left: 40px;
}

.header-area .main-nav .nav li:last-child a,
.background-header .main-nav .nav li:last-child a {
  padding: 0px 20px;
  font-weight: 400;
}

.header-area .main-nav .nav li:last-child a:hover,
.background-header .main-nav .nav li:last-child a:hover {
  color: #4771cb !important;
}

.header-area .main-nav .nav li a {
  display: block;
  font-weight: 500;
  font-size: 15px;
  color: #fff;
  text-transform: capitalize;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
  height: 40px;
  line-height: 40px;
  border: transparent;
  letter-spacing: 1px;
}

.header-area .main-nav .nav li:hover a,
.header-area .main-nav .nav li a.active {
  color: #fff !important;
}

.background-header .main-nav .nav li:hover a,
.background-header .main-nav .nav li a.active {
  color: #fff !important;
  opacity: 1;
}

.header-area .main-nav .nav li.submenu {
  position: relative;
  padding-right: 30px;
}

.header-area .main-nav .nav li.submenu:after {
  font-family: FontAwesome;
  content: "\f107";
  font-size: 12px;
  color: #2a2a2a;
  position: absolute;
  right: 18px;
  top: 12px;
}

.background-header .main-nav .nav li.submenu:after {
  color: #2a2a2a;
}

.header-area .main-nav .nav li.submenu ul {
  position: absolute;
  width: 200px;
  box-shadow: 0 2px 28px 0 rgba(0, 0, 0, 0.06);
  overflow: hidden;
  top: 50px;
  opacity: 0;
  transform: translateY(+2em);
  visibility: hidden;
  z-index: -1;
  transition: all 0.3s ease-in-out 0s, visibility 0s linear 0.3s, z-index 0s linear 0.01s;
}

.header-area .main-nav .nav li.submenu ul li {
  margin-left: 0px;
  padding-left: 0px;
  padding-right: 0px;
}

.header-area .main-nav .nav li.submenu ul li a {
  opacity: 1;
  display: block;
  background: #f7f7f7;
  color: #2a2a2a !important;
  padding-left: 20px;
  height: 40px;
  line-height: 40px;
  -webkit-transition: all 0.3s ease 0s;
  -moz-transition: all 0.3s ease 0s;
  -o-transition: all 0.3s ease 0s;
  transition: all 0.3s ease 0s;
  position: relative;
  font-size: 13px;
  font-weight: 400;
  border-bottom: 1px solid #eee;
}

.header-area .main-nav .nav li.submenu ul li a:hover {
  background: #fff;
  color: #33ccc5 !important;
  padding-left: 25px;
}

.header-area .main-nav .nav li.submenu ul li a:hover:before {
  width: 3px;
}

.header-area .main-nav .nav li.submenu:hover ul {
  visibility: visible;
  opacity: 1;
  z-index: 1;
  transform: translateY(0%);
  transition-delay: 0s, 0s, 0.3s;
}

.header-area .main-nav .menu-trigger {
  cursor: pointer;
  display: block;
  position: absolute;
  top: 33px;
  width: 32px;
  height: 40px;
  text-indent: -9999em;
  z-index: 99;
  right: 40px;
  display: none;
}

.background-header .main-nav .menu-trigger {
  top: 23px;
}

.header-area .main-nav .menu-trigger span,
.header-area .main-nav .menu-trigger span:before,
.header-area .main-nav .menu-trigger span:after {
  -moz-transition: all 0.4s;
  -o-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  transition: all 0.4s;
  background-color: #fff;
  display: block;
  position: absolute;
  width: 30px;
  height: 2px;
  left: 0;
}

.background-header .main-nav .menu-trigger span,
.background-header .main-nav .menu-trigger span:before,
.background-header .main-nav .menu-trigger span:after {
  background-color: #fff;
}

.header-area .main-nav .menu-trigger span:before,
.header-area .main-nav .menu-trigger span:after {
  -moz-transition: all 0.4s;
  -o-transition: all 0.4s;
  -webkit-transition: all 0.4s;
  transition: all 0.4s;
  background-color: #fff;
  display: block;
  position: absolute;
  width: 30px;
  height: 2px;
  left: 0;
  width: 75%;
}

.background-header .main-nav .menu-trigger span:before,
.background-header .main-nav .menu-trigger span:after {
  background-color: #fff;
}

.header-area .main-nav .menu-trigger span:before,
.header-area .main-nav .menu-trigger span:after {
  content: "";
}

.header-area .main-nav .menu-trigger span {
  top: 16px;
}

.header-area .main-nav .menu-trigger span:before {
  -moz-transform-origin: 33% 100%;
  -ms-transform-origin: 33% 100%;
  -webkit-transform-origin: 33% 100%;
  transform-origin: 33% 100%;
  top: -10px;
  z-index: 10;
}

.header-area .main-nav .menu-trigger span:after {
  -moz-transform-origin: 33% 0;
  -ms-transform-origin: 33% 0;
  -webkit-transform-origin: 33% 0;
  transform-origin: 33% 0;
  top: 10px;
}

.header-area .main-nav .menu-trigger.active span,
.header-area .main-nav .menu-trigger.active span:before,
.header-area .main-nav .menu-trigger.active span:after {
  background-color: transparent;
  width: 100%;
}

.header-area .main-nav .menu-trigger.active span:before {
  -moz-transform: translateY(6px) translateX(1px) rotate(45deg);
  -ms-transform: translateY(6px) translateX(1px) rotate(45deg);
  -webkit-transform: translateY(6px) translateX(1px) rotate(45deg);
  transform: translateY(6px) translateX(1px) rotate(45deg);
  background-color: #fff;
}

.background-header .main-nav .menu-trigger.active span:before {
  background-color: #fff;
}

.header-area .main-nav .menu-trigger.active span:after {
  -moz-transform: translateY(-6px) translateX(1px) rotate(-45deg);
  -ms-transform: translateY(-6px) translateX(1px) rotate(-45deg);
  -webkit-transform: translateY(-6px) translateX(1px) rotate(-45deg);
  transform: translateY(-6px) translateX(1px) rotate(-45deg);
  background-color: #fff;
}

.background-header .main-nav .menu-trigger.active span:after {
  background-color: #fff;
}

.header-area.header-sticky {
  min-height: 80px;
}

.header-area .nav {
  margin-top: 30px;
}

.header-area.header-sticky .nav li a.active {
  color: #33ccc5;
}

@media (max-width: 1200px) {
  .header-area .main-nav .nav li {
    padding-left: 12px;
    padding-right: 12px;
  }

  .header-area .main-nav:before {
    display: none;
  }
}

@media (max-width: 992px) {

  .header-area .main-nav .nav li:last-child,
  .background-header .main-nav .nav li:last-child {
    display: none;
  }

  .header-area .main-nav .nav li:nth-child(6),
  .background-header .main-nav .nav li:nth-child(6) {
    padding-right: 0px;
  }
}

@media (max-width: 767px) {
  .background-header .main-nav .nav {
    margin-top: 80px !important;
  }

  .header-area .main-nav .logo {
    color: #1e1e1e;
  }

  .header-area.header-sticky .nav li a:hover,
  .header-area.header-sticky .nav li a.active {
    color: #33ccc5 !important;
    opacity: 1;
  }

  .header-area.header-sticky .nav li.search-icon a {
    width: 100%;
  }

  .header-area {
    background-color: #33ccc5;
    padding: 0px 15px;
    height: 100px;
    box-shadow: none;
    text-align: center;
  }

  .header-area .container {
    padding: 0px;
  }

  .header-area .logo {
    margin-left: 30px;
  }

  .header-area .menu-trigger {
    display: block !important;
  }

  .header-area .main-nav {
    overflow: hidden;
  }

  .header-area .main-nav .nav {
    float: none;
    width: 100%;
    display: none;
    -webkit-transition: all 0s ease 0s;
    -moz-transition: all 0s ease 0s;
    -o-transition: all 0s ease 0s;
    transition: all 0s ease 0s;
    margin-left: 0px;
  }

  .background-header .nav {
    margin-top: 80px;
  }

  .header-area .main-nav .nav li:first-child {
    border-top: 1px solid #eee;
  }

  .header-area.header-sticky .nav {
    margin-top: 100px;
  }

  .header-area .main-nav .nav li {
    width: 100%;
    background: #fff;
    border-bottom: 1px solid #e7e7e7;
    padding-left: 0px !important;
    padding-right: 0px !important;
  }

  .header-area .main-nav .nav li a {
    height: 50px !important;
    line-height: 50px !important;
    padding: 0px !important;
    border: none !important;
    background: #f7f7f7 !important;
    color: #191a20 !important;
  }

  .header-area .main-nav .nav li a:hover {
    background: #eee !important;
    color: #33ccc5 !important;
  }

  .header-area .main-nav .nav li.submenu ul {
    position: relative;
    visibility: inherit;
    opacity: 1;
    z-index: 1;
    transform: translateY(0%);
    transition-delay: 0s, 0s, 0.3s;
    top: 0px;
    width: 100%;
    box-shadow: none;
    height: 0px;
  }

  .header-area .main-nav .nav li.submenu ul li a {
    font-size: 12px;
    font-weight: 400;
  }

  .header-area .main-nav .nav li.submenu ul li a:hover:before {
    width: 0px;
  }

  .header-area .main-nav .nav li.submenu ul.active {
    height: auto !important;
  }

  .header-area .main-nav .nav li.submenu:after {
    color: #3B566E;
    right: 25px;
    font-size: 14px;
    top: 15px;
  }

  .header-area .main-nav .nav li.submenu:hover ul,
  .header-area .main-nav .nav li.submenu:focus ul {
    height: 0px;
  }
}

.header-area .main-nav .nav {
    display: flex !important;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #FDFEFE;
}

/* 
---------------------------------------------
Footer Style
--------------------------------------------- 
*/

footer p {
  text-align: center;
  margin: 30px 0px;
}

footer p a {
  color: #33ccc5;
  transition: all .5s;
}

footer p a:hover {
  color: #4771cb;
}
</style>
