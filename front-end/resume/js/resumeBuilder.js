var bio = {
	"name" : "Jonathan Czerwonka",
	"role" : "Developer",
	"contacts":{
		"mobile":"217-240-1219",
		"email":"jonathan.czerwonka@gmail.com",
		"github":"jdczerwonka",
		"twitter":"@jdczerwonka",
		"location":"Effingham, IL, USA"
	},
	"welcomeMessage":"scientia potentia est",
	"skills":["considering things","following the PayPal mafia", "slicing golf balls","counting pigs"],
	"bioPic": "images/fry.jpg"
};

var projects = {
	"projects":[
		{
			"title":"Portfolio",
			"dates":"May 2015",
			"description":"Built a portfolio to display my apps.",
			"image": "images/portfolio.jpg"
		},
		{
			"title":"Movie Trailer Website",
			"dates":"May 2015",
			"description":"Built a website that displays my favorite movies and tv shows.",
			"image": "images/movie_trailer_website.jpg"			
		},
		{
			"title":"Tournament Results",
			"dates":"May 2015",
			"description":"Built a database and functions to manage a Swiss style tournament.",
			"image": "images/tournament_results.jpg"			
		}
	]
};

var work = {
	"jobs":[
		{
			"employer":"Walk Stock Farm",
			"title":"Financial Analyst",
			"location":"Neoga, IL, USA",
			"dates":"June 2014 - June 2015",
			"description":"Analyze the finacial feasbility of major projects, close the books every month, and create budgets and report cards to measure and benchmark the business."
		},
		{
			"employer":"Monsanto",
			"title":"FP&A Seed Manufacturing Intern",
			"location":"St. Louis, MO, USA",
			"dates":"May 2013 - August 2014",
			"description":"Did budgeting and financial analysis for various departments within the seed manufacturing division."
		}
	]
};

var education = {
	"schools":[
		{
			"name":"University of Illinois Urbana-Champaign",
			"location":"Urbana, IL, USA",
			"degree":"Bachelors",
			"major":"Finace",
			"dates":"August 2012 - May 2014",
			"url":"www.illinois.edu"
		},
		{
			"name":"Lake Land College",
			"location":"Mattoon, IL, USA",
			"degree":"Associates",
			"major":"Business Administration",
			"dates":"January 2011 - May 2012",
			"url":"http://www.lakeland.cc.il.us/"
		}
	],
	"onlineCourses":[
		{
			"title":"Front-End Web Developer",
			"school":"Udacity",
			"dates":"May 2015 - Current",
			"url":"https://www.udacity.com/course/front-end-web-developer-nanodegree--nd001"

		},
		{
			"title":"Full Stack Web Developer",
			"school":"Udacity",
			"dates":"May 2015 - Current",
			"url":"https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004"
		}
	]
};

bio.display = function() {
	if(bio.role){
		var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
		$("#header").prepend(formattedRole);
	}

	if(bio.name){
		var formattedName = HTMLheaderName.replace("%data%", bio.name);
		$("#header").prepend(formattedName);
	}

	if(bio.contacts){
		for(var contact in bio.contacts){
			var formattedContact = HTMLcontactGeneric.replace("%data%", bio.contacts[contact]).replace("%contact%",contact);
			$("#topContacts").append(formattedContact);
			$("#footerContacts").append(formattedContact);
		}
	}

	if(bio.bioPic){
		var formattedbioPic = HTMLbioPic.replace("%data%", bio.bioPic);
		$("#header").append(formattedbioPic);
	}

	if(bio.welcomeMessage){
		var formattedWelcome = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);
		$("#header").append(formattedWelcome);
	}

	if(bio.skills){
		$("#header").append(HTMLskillsStart);

		for(var skill in bio.skills){
			var formattedSkill = HTMLskills.replace("%data%", bio.skills[skill]);
			$("#skills").append(formattedSkill);
		}
	}
}

work.display = function() {
	if(work.jobs){
		for(var job in work.jobs){
			$("#workExperience").append(HTMLworkStart);
			var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
			var formattedTitle = HTMLworkTitle.replace("%data%", work.jobs[job].title);
			var formattedEmployerTitle = formattedEmployer + formattedTitle;
			$(".work-entry:last").append(formattedEmployerTitle);

			var formattedDates = HTMLworkDates.replace("%data%", work.jobs[job].dates);
			$(".work-entry:last").append(formattedDates);

			var formattedDescription = HTMLworkDescription.replace("%data%", work.jobs[job].description);
			$(".work-entry:last").append(formattedDescription);
		}
	}
}

projects.display = function() {
	if(projects.projects){
		for(var project in projects.projects){
			$("#projects").append(HTMLprojectStart);

			var formattedTitle = HTMLprojectTitle.replace("%data%", projects.projects[project].title);
			$(".project-entry:last").append(formattedTitle);

			var formattedDates = HTMLprojectDates.replace("%data%", projects.projects[project].dates);
			$(".project-entry:last").append(formattedDates);

			var formattedDescription = HTMLprojectDescription.replace("%data%", projects.projects[project].description);
			$(".project-entry:last").append(formattedDescription);

			var formattedImage = HTMLprojectImage.replace("%data%", projects.projects[project].image);
			$(".project-entry:last").append(formattedImage);
		}
	}
}

education.display = function() {
	if(education.schools){
		for(var school in education.schools){
			$("#education").append(HTMLschoolStart);
			var formattedName = HTMLschoolName.replace("%data%", education.schools[school].name);
			var formattedDegree = HTMLschoolDegree.replace("%data%", education.schools[school].degree);
			var formattedNameDegree = formattedName + " " + formattedDegree;
			$(".education-entry:last").append(formattedNameDegree);

			var formattedDates = HTMLschoolDates.replace("%data%", education.schools[school].dates);
			$(".education-entry:last").append(formattedDates);

			var formattedLocation = HTMLschoolLocation.replace("%data%", education.schools[school].location);
			$(".education-entry:last").append(formattedLocation);

			var formattedMajor = HTMLschoolMajor.replace("%data%", education.schools[school].major);
			$(".education-entry:last").append(formattedMajor);
		}
	}

	if(education.onlineCourses){
		$("#education").append(HTMLonlineClasses);

		for(var course in education.onlineCourses){
			$("#education").append(HTMLschoolStart);
			var formattedTitle = HTMLonlineTitle.replace("%data%", education.onlineCourses[course].title);
			var formattedSchool = HTMLonlineSchool.replace("%data%", education.onlineCourses[course].school);
			var formattedTitleSchool = formattedTitle + " " + formattedSchool
			$(".education-entry:last").append(formattedTitleSchool);

			var formattedDates = HTMLonlineDates.replace("%data%", education.onlineCourses[course].dates);
			$(".education-entry:last").append(formattedDates);

			var formattedURL = HTMLonlineURL.replace("%data%", education.onlineCourses[course].url);
			$(".education-entry:last").append(formattedURL);
		}
	}
}

bio.display();
work.display();
projects.display();
education.display();

$("#mapDiv").append(googleMap);

// function inName(name){
// 	name = name.trim().split(" ");
// 	name[1] = name[1].toUpperCase();
// 	name[0] = name[0].slice(0,1).toUpperCase() + name[0].slice(1).toLowerCase();

// 	return name[0] + " " + name[1];
// }

// $("#main").append(internationalizeButton);