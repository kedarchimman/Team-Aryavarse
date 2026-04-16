const FOLDERS = {

  //banner
  banner:'banner_img',

  //about
  about:'About',

  // men + women
  parallel: 'scrub_suits_models_parallel',
  models: 'parallel_models',

  collarBoy: 'Collar_scrub_suits/boys',

  // women
  collarGirl: 'Collar_scrub_suits/girl',
  vNeckModel: 'V-neck scrubs suit/Womens model',
  vNeckSide: 'V-neck scrubs suit/Womens side view',
  vNeckHanger: 'V-neck scrubs suit/hanger scrubs',

  // aprons
  apronFullSleeve: 'Doctors_Aprons/Doctor_apron_full_length_sleeves',
  apronThreeQuarter: 'Doctors_Aprons/Doctor_apron_full_length_3-4_sleeves',
  apronHalf: 'Doctors_Aprons/Doctor_apron_half_length_hs',
}

//root path (assets = root)
const rootPath = '../assets'

// preload all images (Vite)
const images = import.meta.glob('../assets/**/*', {
  eager: true,
  import: 'default'
})

export const getImage = (folder, filename) => {
  const folderPath = FOLDERS[folder]

  //invalid folder check
  if (!folderPath) {
    console.warn(`Unknown folder: ${folder}`)
    return ''
  }

  //rootPath + folder + filename 
  const path = `${rootPath}/${folderPath}/${filename}`

  //return matched image URL
  return images[path] || ''
}

// shortcuts (easy use)

//banner
export const bannerImg = (f) => getImage('banner', f)

//about
export const aboutImg = (f) => getImage('about', f)

export const parallelImg = (f) => getImage('parallel', f)
export const modelImg    = (f) => getImage('models', f)

export const collarBoyImg  = (f) => getImage('collarBoy', f)

export const collarGirlImg  = (f) => getImage('collarGirl', f)
export const vNeckModelImg  = (f) => getImage('vNeckModel', f)
export const vNeckSideImg   = (f) => getImage('vNeckSide', f)
export const vNeckHangerImg = (f) => getImage('vNeckHanger', f)

export const apronFullImg  = (f) => getImage('apronFullSleeve', f)
export const apronThreeImg = (f) => getImage('apronThreeQuarter', f)
export const apronHalfImg  = (f) => getImage('apronHalf', f)