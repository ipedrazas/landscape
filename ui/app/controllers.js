app.controller('main', function($scope, api) {

    $scope.editing = null;

    $scope.rels =
    [
        { id: 1, type: "People", name: "USES" },
        { id: 2, type: "People", name: "ADMINISTERS" },
        { id: 3, type: "People", name: "SUPPORTS" },
        { id: 4, type: "Components", name: "CONNECTS" },
        { id: 5, type: "Components", name: "IS_PART" }
    ];


    var getLinks = function(item){
        api.getLinks(item.id).success(function(data){
            item.children = data.children;
        });
    };

    var getApps = function(){
        api.getApplications().success(function(data){
                $scope.applications = data.applications;
          });
    }

    var link = function(item) {
        $scope.editingPerson = null;
        $scope.editingComponent = null;

        if(item.type == 'Person'){
            $scope.editingPerson = item;
        }
      if(item.type == 'Component'){
            $scope.editingComponent = item;
        }
        var rels = [];

        getLinks(item);
        getApps();

    };

    $scope.editPerson = function(person_id){
        console.log(person_id);
    };

    $scope.savePerson = function() {
        if($scope.personName.length > 2){
            var person = {name: $scope.personName};
            var res = api.addPerson(person).success(function(data){
                $scope.getPeople();
                $scope.personName = "";
            });
        }

    };

    $scope.getPeople = function(){
         var stored_people = api.getPeople().success(function(data){
                _.each(data.people, function(person){
                    person = link(person);
                })
                $scope.people = data.people;
                resetEditing();
          });
    };


    $scope.link = function(item){
        link(item);
    }

    var resetEditing = function(){
        $scope.editingPerson = null;
         $scope.editingComponent = null;
    };

    $scope.saveRel = function(type){
        var source = {};

        if(type == 'Person'){
            source = $scope.editingPerson;
        }
      if(type == 'Component'){
            source = $scope.editingComponent;
        }
        resetEditing();
        var link = {
            source: source.id,
            source_label: source.type,
            target: $scope.rel.target.id,
            rel: $scope.rel.label.name,
            target_label: $scope.rel.target.type
        };
        api.addLink(link).success(function(data){
            resetEditing();
            getLinks(link);
            getApps();
        });
    };


    $scope.saveApplication= function() {
        var application = {name: $scope.applicationName};
        var res = api.addApplication(application).success(function(data){
                $scope.getApplications();
                $scope.applicationName = "";
          });

    }

    $scope.getApplications = function(){
         var apps = api.getApplications().success(function(data){
                $scope.applications = data.applications;
          });
    };

    $scope.saveComponent = function() {
        var comp = {name: $scope.componentName};
        var res = api.addComponent(comp).success(function(data){
                $scope.getComponents();
                $scope.componentName = "";
          });
    }

    $scope.getComponents = function(){
         var components = api.getComponents().success(function(data){
                console.log(data);
                _.each(data.components, function(comp){
                    comp = link(comp);
                })
                $scope.components = data.components;
                resetEditing();
          });
    };

    $scope.getLinks = function(item){
        console.log(item);
        api.getLinks(item.id).success(function(data){
            console.log(data);
            item.children = data.children;
        });
    };

    $scope.getPeople();
    $scope.getApplications();
    $scope.getComponents();

});
