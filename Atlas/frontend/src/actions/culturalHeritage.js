export const fetchCH = () => {
  return {
    type: 'FETCH_CULTURAL_HERITAGES'
  }
}

export const fetchNearbyCH = () => {
  return{
    type: 'FETCH_NEARBY_CHS'
  }
}

export const clearAddChErrors = () => {
  return{
    type: 'CLEAR_ADD_CH_ERRORS'
  }
}

export const updateLocation =(loc) =>{
  return{
    type: 'UPDATE_USER_LOCATION',
    data: loc
  }
}

export const dragMap = (loc) => {
  return{
    type: 'MAP_DRAGGED',
    data:loc
  }
}

export const mouseOverItem = (id) => {
  return {
    type: 'MOUSE_OVER_ITEM',
    data: id
  }
}

export const mouseOffItem = () => {
  return {
    type: 'MOUSE_OFF_ITEM'
  }
}

export const loadSingleItem = () => {
  return {
    type: 'LOAD_CULTURAL_HERITAGE',
  }
}

export const finishFetchingCH = () => {
  return {
    type: 'FINISH_FETCHING_CULTURAL_HERITAGES'
  }
}

export const finishFetchingNearbyCH = () => {
  return {
    type: 'FINISH_FETCHING_NEARBY_CHS'
  }
}

export const uploadImage = (imageLink) => {
    return {
        type: 'IMAGE_URL_UPLOADED',
        data: imageLink
    }
}

export const updatingGetCH = (culturalHeritages) => {
  return {
    type: 'UPDATE_CULTURAL_HERITAGES',
    data: culturalHeritages
  }
}

export const updatingNearbyCH = (nearbyCHS) => {
  return {
    type: 'UPDATE_NEARBY_CHS',
    data: nearbyCHS
  }
}

export const updateCHInput = (name, value) => {
  return {
    type: 'UPDATE_CULTURAL_HERITAGE_INPUT',
    name,
    value
  }
}

export const addCHFetch = () => {
  return {
    type: 'ADD_CH_FETCH'
  }
}

export const addCHSuccess = () => {
  return {
    type: 'ADD_CH_SUCCESS'
  }
}

export const addCHFail = (errors) => {
  return {
    type: 'ADD_CH_FAIL',
    errors
  }
}

export const toggleAddCHModal = () => {
  return {
    type: 'TOGGLE_ADD_CH_MODAL'
  }
}

export const clearAddCHInputs = () => {
  return {
    type: 'CLEAR_ADD_CH_INPUTS'
  }
}

export const addCHTag = (name) => {
  return {
    type: 'ADD_CH_TAG',
    data: name
  }
}

export const deleteCHTag = (id) => {
  return {
    type: 'DELETE_CH_TAG',
    data: id
  }
}

export const closeHelp = () => {
  return {
    type: 'CLOSE_HELP'
  }
}

export const updateCHPaginationNext = (nextUrl) => {
  return {
    type: 'UPDATE_CH_PAGINATION_NEXT',
    data: nextUrl
  }
}

export const loadMoreCH = (data) => {
  return {
    type: 'LOAD_MORE_CH',
    data
  }
}

export const updateCommentInput = (data) => {
  return {
    type: 'UPDATE_COMMENT_INPUT',
    data
  }
}

export const startLoadMore = () => {
  return {
    type: 'START_LOAD_MORE'
  }
}

export const finishLoadMore = () => {
  return {
    type: 'FINISH_LOAD_MORE'
  }
}

export const disableLoadMore = () => {
  return {
    type: 'DISABLE_LOAD_MORE'
  }
}

export const enableLoadMore = () => {
  return {
    type: 'ENABLE_LOAD_MORE'
  }
}

export const updateCulturalHeritage = (id, data) => {
  return {
    type: 'UPDATE_CULTURAL_HERITAGE',
    data: {
      id,
      data
    }
  }
}

export const updateRecommendations = (data) => {
  return {
    type: 'UPDATE_RECOMMENDATIONS',
    data
  }
}


export const deleteCulturalHeritage = (data) => {
    return {
        type: 'DELETE_CULTURAL_HERITAGE',
        data
    }
}

export const startUpdateRecommendation = () => {
    return {
        type: 'START_UPDATE_RECOMMENDATION',
    }
}

export const showAnnotation = (a) => {
  return {
    type: 'SHOW_ANNOTATION',
    data: a.id
  }
}

export const hideAnnotation = (a) => {
  return {
    type: 'HIDE_ANNOTATION',
    data: a.id
  }
}

export const updateAnnotationInput = (input_type, newInput) => {
  return {
    type: 'UPDATE_ANNOTATION_INPUT',
    data: {
      input_type,
      newInput
    }
  }
}

export const createAnnotation = (data) => {
  return {
    type: 'CREATE_ANNOTATION',
    data
  }
}

export const openAnnotationInput = (x, y) => {
  return {
    type: 'OPEN_ANNOTATION_INPUT',
    data: {
      x,
      y
    }
  }
}

export const closeAnnotationInput = () => {
  return {
    type: 'CLOSE_ANNOTATION_INPUT'
  }
}

export const hideAnnotations = () => {
  return {
    type: 'HIDE_ANNOTATIONS'
  }
}

export const updateAnnotations = (data) => {
  return {
    type: 'UPDATE_ANNOTATIONS',
    data
  }
}
