// Oh bother, let's try this a little differently.
// Nexus Clash profile Lookup v0.6
// This utilizes the NC profile API to search characters by name
// I am new at Javascript, so, uhm, sorry probably.
//written by plscks
var input = document.getElementById("inPut");
var expBadges = [];
var masterSkillsList = [];
var masterBadges = [];
var masterInfo = [];
var masterSpells = [];

input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("inButton").click();
  }
});

function nameGrab() {
  // Gets the text the user has typed into the input field
  var charName = document.getElementById("inPut").value;
  charName = charName.replace(/\s+/g, '%20');
  return charName
}

function resetFields() {
  document.getElementById('charName').innerHTML = "";
  document.getElementById('charLevel').innerHTML = "";
  document.getElementById('charClass').innerHTML = "";
  document.getElementById('aliveStatus').innerHTML = "";
  document.getElementById('charPosition').innerHTML = "";
  document.getElementById('charFaction').innerHTML = "";
  document.getElementById('charInfo2').innerHTML = "";
  document.getElementById('physDescription').innerHTML = "";
  document.getElementById('personalDescription').innerHTML = "";
  document.getElementById('charAlc').innerHTML = "-";
  document.getElementById('charAngel').innerHTML = "-";
  document.getElementById('charBooks').innerHTML = "-";
  document.getElementById('charDamDeal').innerHTML = "-";
  document.getElementById('charDamTake').innerHTML = "-";
  document.getElementById('charDeaths').innerHTML = "-";
  document.getElementById('charDemons').innerHTML = "-";
  document.getElementById('charDoorsDest').innerHTML = "-";
  document.getElementById('charDoorsRep').innerHTML = "-";
  document.getElementById('charFood').innerHTML = "-";
  document.getElementById('charHp').innerHTML = "-";
  document.getElementById('charItCraft').innerHTML = "-";
  document.getElementById('charItRep').innerHTML = "-";
  document.getElementById('charKills').innerHTML = "-";
  document.getElementById('charLocks').innerHTML = "-";
  document.getElementById('charPets').innerHTML = "-";
  document.getElementById('charPills').innerHTML = "-";
  document.getElementById('charPowerRem').innerHTML = "-";
  document.getElementById('charPowerRest').innerHTML = "-";
  document.getElementById('charTargets').innerHTML = "-";
  document.getElementById('exploreBadges').innerHTML = "";
  return;
}

async function lookup() {
  // looks up name in the NC profile API, then stores json data
  resetFields();
  name  = nameGrab();
  var requestUrl = "https://www.nexusclash.com/modules.php?name=Character&charname=" + name + "&format=json";
  var corsUrl = 'https://cors.plscks.workers.dev/?' + requestUrl

  var jsonData = await getData2(corsUrl);

  if (jsonData.result.character.id == 0) {
    document.getElementById('charName').innerHTML = "No character exists by this name";
    document.getElementById('charInfo2').innerHTML = "<img src='nochar.png'>";
    return;
  }

  var ncProfLink = "https://www.nexusclash.com/modules.php?name=Game&op=character&id=";
  var namePrefix = jsonData.result.character.name.prefix;
  var nameName = jsonData.result.character.name.name;
  var nameSuffix = jsonData.result.character.name.suffix;
  var nameDomain = jsonData.result.character.name.domain;
  var fullName = namePrefix + nameName + nameSuffix + nameDomain;
  masterSkillsList = jsonData.result.character.skills;
  masterInfo = [jsonData.result.character.level, jsonData.result.character.classes];
  masterSpells = jsonData.result.character.spells;

  document.getElementById('charName').innerHTML = " <a href='" + ncProfLink + jsonData.result.character.id + "'>[profile]</a>" + " " + fullName;
  document.getElementById('charLevel').innerHTML = jsonData.result.character.level;
  var currentClass = jsonData.result.character.classes[jsonData.result.character.classes.length - 1];
  document.getElementById('charClass').innerHTML = currentClass;

  if (jsonData.result.character.status.alive == true) {
    document.getElementById('aliveStatus').innerHTML = "<span style='color: #28e713;'>This character is alive</span>";
  } else {
    document.getElementById('aliveStatus').innerHTML = "<span style='color: #FD1D53;'>This character is a formless spirit, floating above the planes, dead.</span>"
  }

  if (jsonData.result.character.faction.id == 0) {
    document.getElementById('charPosition').innerHTML = "";
    document.getElementById('charFaction').innerHTML = nameName + " is not currently in a faction";
  } else {
    var factionLink = jsonData.result.character.faction.url;
    document.getElementById('charPosition').innerHTML = "<a href='" + factionLink + "'>[link]</a>" + " " + jsonData.result.character.faction.rank + " in ";
    document.getElementById('charFaction').innerHTML = jsonData.result.character.faction.name;
  }

  document.getElementById('charInfo2').innerHTML = "<img src='" + jsonData.result.character.avatar.url + "' height='250' width='250'>";
  document.getElementById('physDescription').innerHTML = jsonData.result.character.description.physical;
  document.getElementById('personalDescription').innerHTML = jsonData.result.character.description.personal;
  await badgeParse(jsonData.result.character.badges, nameName);
}

async function badgeParse(badges, name) {
  masterBadges = badges;
  var alcoholBadges = {
    1: "Low Tolerance",
    2: "Frat Boy",
    3: "Alcoholic",
    4: "Sinatra",
    5: "Friend of Bill"
  }
  var alcoholMax = badgeMax(badges, alcoholBadges, 0);

  var angelBadges = {
    1: "Perverter",
    2: "Ruiner",
    3: "Nightmare Whisperer",
    4: "Voice of Armageddon",
    5: "The End of Hope"
  }
  var angelMax = badgeMax(badges, angelBadges, 0);

  var booksBadges = {
    1: "Reader",
    2: "Bookworm",
    3: "Librarian",
    4: "Bibliophile",
    5: "Teachers Pet"
  }
  var booksMax = badgeMax(badges, booksBadges, 0);

  var damDealBadges = {
    1: "Crusher",
    2: "Smasher",
    3: "Bloodletter",
    4: "Assassin",
    5: "Surgeons Lament",
    6: "Widowmaker"
  }
  var damDealMax = badgeMax(badges, damDealBadges, 1);

  var damTakeBadges = {
    1: "Punching Bag",
    2: "Bruised",
    3: "Crushed",
    4: "All Stitched Up",
    5: "Keeping Healers in Business",
    6: "Constantly in Traction"
  }
  var damTakeMax = badgeMax(badges, damTakeBadges, 1);

  var deathsBadges = {
    1: "Buried",
    2: "Wormfood",
    3: "Aspect Hunter",
    4: "Lich Pet",
    5: "Coffinmakers Friend"
  }
  var deathsMax = badgeMax(badges, deathsBadges, 0);

  var demonsBadges = {
    1: "Cleanser",
    2: "Demonslayer",
    3: "Hammer of Light",
    4: "Justicebringer",
    5: "Blade of the Word"
  }
  var demonsMax = badgeMax(badges, demonsBadges, 0);

  var doorsDestBadges = {
    1: "Opportunity Knocks",
    2: "Big Bad Wolf",
    3: "Heres Johnny",
    4: "Landshark",
    5: "Homewrecker"
  }
  var doorsDestMax = badgeMax(badges, doorsDestBadges, 0);

  var doorsRepBadges = {
    1: "Apprentice Carpenter",
    2: "Woodworker",
    3: "Journeyman Carpenter",
    4: "Architect",
    5: "Master Carpenter"
  }
  var doorsRepMax = badgeMax(badges, doorsRepBadges, 0);

  var foodBadges = {
    1: "Taste Tester",
    2: "Gourmand",
    3: "Glutton",
    4: "Masticator",
    5: "Food Critic"
  }
  var foodMax = badgeMax(badges, foodBadges, 0);

  var healBadges = {
    1: "Medic",
    2: "Doctor",
    3: "Surgeon",
    4: "Healer",
    5: "Bodyweaver",
    6: "Lifesaver"
  }
  var healMax = badgeMax(badges, healBadges, 1);

  var itemsCraBadges = {
    1: "Sweat Shop Worker",
    2: "Journeyman Blacksmith",
    3: "Factory Foreman",
    4: "Artisan",
    5: "Artifex"
  }
  var itemsCraMax = badgeMax(badges, itemsCraBadges, 0);

  var itemsRepBadges = {
    1: "Tinker",
    2: "Mender",
    3: "Fixer",
    4: "Handyman",
    5: "80s Action Hero"
  }
  var itemsRepMax = badgeMax(badges, itemsRepBadges, 0);

  var killsBadges = {
    1: "Killer",
    2: "Warrior",
    3: "Disciple of Death",
    4: "Master of Death",
    5: "Gravemaker"
  }
  var killsMax = badgeMax(badges, killsBadges, 0);

  var locksBadges = {
    1: "Thief",
    2: "Burglar",
    3: "Second-Story Man",
    4: "Locksmith",
    5: "Master of Tumblers"
  }
  var locksMax = badgeMax(badges, locksBadges, 0);

  var petsBadges = {
    1: "Dogkiller",
    2: "Exterminator",
    3: "Pest Control",
    4: "Trophy Hunter",
    5: "Director of Animal Testing"
  }
  var petsMax = badgeMax(badges, petsBadges, 0);

  var pillsBadges = {
    1: "I Have a Headache",
    2: "Pill-popper",
    3: "Living the High Life",
    4: "Monster Addict",
    5: "Slave to the Habit"
  }
  var pillsMax = badgeMax(badges, pillsBadges, 0);

  var powRemBadges = {
    1: "Wiresnipper",
    2: "Fusebreaker",
    3: "Circuitbreaker",
    4: "Blackout",
    5: "Degenerate"
  }
  var powRemMax = badgeMax(badges, powRemBadges, 0);

  var powResBadges = {
    1: "Apprentice Electrician",
    2: "Fusemaker",
    3: "Journeyman Electrician",
    4: "Circuitmaker",
    5: "Master Electrician"
  }
  var powResMax = badgeMax(badges, powResBadges, 0);

  var targetsBadges = {
    1: "Barn Assassin",
    2: "Sharpshooter",
    3: "Deadeye",
    4: "Gunslinger",
    5: "Hickok"
  }
  var targetsMax = badgeMax(badges, targetsBadges, 0);

  var exploreBadges = ["A New Chapter", "Academic Probation", "All In The Family", "And I Must Scream", "At All Costs", "Baraas Ascends", "Birthing Pool", "Broken Alliance", "Broken Promises", "Circumnavigation", "Citadel", "Clinging to Life", "Cloudwatching", "Cops and Robbers", "Dedicated Few", "Enthroned", "Explosive Yield", "Fall of the Watcher", "Four Corners", "Fragmented Return", "Halls of the Scholar", "Halls of Wrath", "Idle Hands", "In The Name Of Science", "Institute of Arts", "Into the Dark", "Last Confession", "Reasons to Live", "Remorse", "Stolen Victory", "Tapestry of Time", "The Earth Shudders", "The Legend", "The Little King", "The Rise of Kafa-El", "The Voice", "Under The Boot ", "Untouched Wilderness ", "Well of Truth", "What Once Was Lost"];

  exploreBadges = exploreBadges.filter(val => badges.includes(val));
  expBadges = exploreBadges;

  var badgeNumNorm = ["< 10", "10 - 49", "50 - 99", "100 - 499", "500 - 999", "≥ 1000"];
  var badgeNumDam = ["< 500", "500 - 999", "1000 - 4999", "5000 - 9999", "10000 - 49999", "50000 - 99999", "≥ 100000"];
  var badgeNumHeal = ["< 500", "500 - 999", "1000 - 4999", "5000 - 9999", "10000 - 14999", "15000 - 19999", "≥ 20000"];

  document.getElementById('charAlc').innerHTML = badgeNumNorm[alcoholMax];
  document.getElementById('charAngel').innerHTML = badgeNumNorm[angelMax];
  document.getElementById('charBooks').innerHTML = badgeNumNorm[booksMax];
  document.getElementById('charDamDeal').innerHTML = badgeNumDam[damDealMax];
  document.getElementById('charDamTake').innerHTML = badgeNumDam[damTakeMax];
  document.getElementById('charDeaths').innerHTML = badgeNumNorm[deathsMax];
  document.getElementById('charDemons').innerHTML = badgeNumNorm[demonsMax];
  document.getElementById('charDoorsDest').innerHTML = badgeNumNorm[doorsDestMax];
  document.getElementById('charDoorsRep').innerHTML = badgeNumNorm[doorsRepMax];
  document.getElementById('charFood').innerHTML = badgeNumNorm[foodMax];
  document.getElementById('charHp').innerHTML = badgeNumHeal[healMax];
  document.getElementById('charItCraft').innerHTML = badgeNumNorm[itemsCraMax];
  document.getElementById('charItRep').innerHTML = badgeNumNorm[itemsRepMax];
  document.getElementById('charKills').innerHTML = badgeNumNorm[killsMax];
  document.getElementById('charLocks').innerHTML = badgeNumNorm[locksMax];
  document.getElementById('charPets').innerHTML = badgeNumNorm[petsMax];
  document.getElementById('charPills').innerHTML = badgeNumNorm[pillsMax];
  document.getElementById('charPowerRem').innerHTML = badgeNumNorm[powRemMax];
  document.getElementById('charPowerRest').innerHTML = badgeNumNorm[powResMax];
  document.getElementById('charTargets').innerHTML = badgeNumNorm[targetsMax];

  if (exploreBadges.length == 0) {
    document.getElementById('exploreBadges').innerHTML = name + " has not found any exploration badges yet<p> 40 badges left to find <a class='charExpBadges' id='badgeButton' onClick='badgeLink()' href=hypermap.html> Set Hypermap to Missing Badges </a><a class='charExpBadges' id='planButton' onClick='planLink()' href=chargen_b4_v2_5.html> Set Planner to current character </a>";
  } else if (exploreBadges.length == 40) {
    document.getElementById('exploreBadges').innerHTML = "Exploration Badges obtained: <p>" + exploreBadges + "<p> All exploration badges obtained. <a class='charExpBadges' id='planButton' onClick='planLink()' href=chargen_b4_v2_5.html> Set Planner to current character </a>";
  } else {
    badgesLeft = 40 - exploreBadges.length;
    document.getElementById('exploreBadges').innerHTML = "Exploration Badges obtained: <p>" + exploreBadges + "<p>" + badgesLeft + " badges left to find <a class='charExpBadges' id='badgeButton' onClick='badgeLink()' href=hypermap.html> Set Hypermap to Missing Badges </a><a class='charExpBadges' id='planButton' onClick='planLink()' href=chargen_b4_v2_5.html> Set Planner to current character </a>";
  }
}

function badgeLink() {
  localStorage.setItem("expBadges", JSON.stringify(expBadges));
}

function planLink() {
  localStorage.setItem("masterSkills", JSON.stringify(masterSkillsList));
  localStorage.setItem("masterBadges", JSON.stringify(masterBadges));
  localStorage.setItem("masterInfo", JSON.stringify(masterInfo));
  localStorage.setItem("masterSpells", JSON.stringify(masterSpells));
}

function badgeMax(all, category, n) {
  if (n == 1) {
    var j = 7;
  } else {
    var j = 6;
  }

  for (i = 1; i < j; i++) {
    if (all.includes(category[i]) == false) {
      delete category[i];
    }
  }
  var categoryReal = Object.keys(category).map(Number);
  var categoryMax = Math.max.apply(null, categoryReal);
  if (isFinite(categoryMax) == false) {
    return 0;
  } else {
    return categoryMax;
  }
}

async function getData2(corsUrl) {
    const response = await fetch(corsUrl, {});
    const json = await response.json();

    return json;
}
