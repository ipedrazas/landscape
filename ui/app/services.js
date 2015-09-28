app.factory("api", function($q, $http) {

  var getPeople = function() {
    return $http.get(API_HOST + '/people');
  };

  var addPerson = function(data){
    return $http.post(API_HOST + '/people', data);
  };

  var addLink = function(data){
      return $http.post(API_HOST + '/links', data)
  };

  var addApplication = function(data){
    return $http.post(API_HOST + '/applications', data);
  };

  var getApplications = function() {
    return $http.get(API_HOST + '/applications');
  };

    var addComponent = function(data){
    return $http.post(API_HOST + '/components', data);
  };

  var getComponents = function() {
    return $http.get(API_HOST + '/components');
  };

  var connects = function(data){
    return $http.post(API_HOST + '/rel/connects', data);
  };

var isPart = function(data){
    return $http.post(API_HOST + '/rel/ispart', data);
  };

  var getLinks = function(item_id) {
    return $http.get(API_HOST + '/links/' + item_id);
  };

  return {
    getApplications: getApplications,
    addLink: addLink,
    getLinks: getLinks,
    addApplication: addApplication,
    getComponents: getComponents,
    addComponent: addComponent,
    getPeople: getPeople,
    addPerson: addPerson,
    getApplications: getApplications,
    connects: connects,
    isPart: isPart
  };
});
