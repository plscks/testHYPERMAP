// Oh bother, let's try this a little differently.
// Nexus Clash profile Lookup v0.2
// This utilizes the NC profile API to search characters by name
// I am new at this, so, uhm, sorry probably.
//written by plscks
function nameGrab() {
  // Gets the text the user has typed into the input field
  var charName = document.getElementById("inPut").value;
  charName = charName.replace(/\s+/g, '%20');
  return charName
}

async function lookup() {
  // looks up name in the NC profile API, then stores json data
  name = nameGrab();
  var requestUrl = "https://www.nexusclash.com/modules.php?name=Character&charname=" + name + "&format=json";
  var corsUrl = 'https://cors-anywhere.herokuapp.com/' + requestUrl

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

  document.getElementById('charInfo2').innerHTML = "<img src='" + jsonData.result.character.avatar.url + "'>";
  document.getElementById('physDescription').innerHTML = jsonData.result.character.description.physical;
  document.getElementById('personalDescription').innerHTML = jsonData.result.character.description.personal;
  await badgeParse(jsonData.result.character.badges, nameName);
}

async function badgeParse(badges, name) {
  var alcoholBadges = ["Low Tolerance", "Frat Boy", "Alcoholic", "Sinatra", "Friend of Bill"];
  var angelBadges = ["Perverter", "Ruiner", "Nightmare Whisperer", "Voice of Armageddon", "The End of Hope"];
  var booksBadges = ["Reader", "Bookworm", "Librarian", "Bibliophile", "Teachers Pet"];
  var damDealBadges = ["Crusher", "Smasher", "Bloodletter", "Assassin", "Surgeons Lament", "Widowmaker"];
  var damTakeBadges = ["Punching Bag", "Bruised", "Crushed", "All Stitched Up", "Keeping Healers in Business", "Constantly in Traction"];
  var deathsBadges = ["Buried", "Wormfood", "Aspect Hunter", "Lich Pet", "Coffinmakers Friend"];
  var demonsBadges = ["Cleanser", "Demonslayer", "Hammer of Light", "Justicebringer", "Blade of the Word"];
  var doorsDestBadges = ["Opportunity Knocks", "Big Bad Wolf", "Heres Johnny", "Landshark", "Homewrecker"];
  var doorsRepBadges = ["Apprentice Carpenter", "Woodworker", "Journeyman Carpenter", "Architect", "Master Carpenter"];
  var foodBadges = ["Taste Tester", "Gourmand", "Glutton", "Masticator", "Food Critic"];
  var healBadges = ["Medic", "Doctor", "Surgeon", "Healer", "Bodyweaver", "Lifesaver"];
  var itemsCraBadges = ["Sweat Shop Worker", "Journeyman Blacksmith", "Factory Foreman", "Artisan", "Artifex"];
  var itemsRepBadges = ["Tinker", "Mender", "Fixer", "Handyman", "80s Action Hero"];
  var killsBadges = ["Killer", "Warrior", "Disciple of Death", "Master of Death", "Gravemaker"];
  var locksBadges = ["Thief", "Burglar", "Second-Story Man", "Locksmith", "Master of Tumblers"];
  var petsBadges = ["Dogkiller", "Exterminator", "Pest Control", "Trophy Hunter", "Director of Animal Testing"];
  var pillsBadges = ["I Have a Headache", "Pill-popper", "Living the High Life", "Monster Addict", "Slave to the Habit"];
  var powRemBadges = ["Wiresnipper", "Fusebreaker", "Circuitbreaker", "Blackout", "Degenerate"];
  var powResBadges = ["Apprentice Electrician", "Fusemaker", "Journeyman Electrician", "Circuitmaker", "Master Electrician"];
  var targetsBadges = ["Barn Assassin", "Sharpshooter", "Deadeye", "Gunslinger", "Hickok"];
  var exploreBadges = ["A New Chapter", "Academic Probation", "All In The Family", "And I Must Scream", "At All Costs", "Baraas Ascends", "Birthing pool", "Broken Alliance", "Broken Promises", "Circumnavigation", "Citadel", "Clinging to Life", "Cloudwatching", "Cops and Robbers", "Dedicated Few", "Enthroned", "Explosive Yield", "Fall of the Watcher", "Four Corners", "Fragmented Return", "Halls of the Scholar", "Halls of Wrath", "Idle hands", "In The Name Of Science", "Institute of Arts", "Into the Dark", "Last Confession", "Reasons to Live", "Remorse", "Stolen Victory", "Tapestry of Time", "The Earth Shudders", "The Legend", "The Little King", "The Rise of Kafa-El", "The Voice", "Under The Boot", "Untouched Wilderness", "Well of Truth", "What Once Was Lost"];

  alcoholBadges = alcoholBadges.filter(val => badges.includes(val));
  angelBadges = angelBadges.filter(val => badges.includes(val));
  booksBadges = booksBadges.filter(val => badges.includes(val));
  damDealBadges = damDealBadges.filter(val => badges.includes(val));
  damTakeBadges = damTakeBadges.filter(val => badges.includes(val));
  deathsBadges = deathsBadges.filter(val => badges.includes(val));
  demonsBadges = demonsBadges.filter(val => badges.includes(val));
  doorsDestBadges = doorsDestBadges.filter(val => badges.includes(val));
  doorsRepBadges = doorsRepBadges.filter(val => badges.includes(val));
  foodBadges = foodBadges.filter(val => badges.includes(val));
  healBadges = healBadges.filter(val => badges.includes(val));
  itemsCraBadges = itemsCraBadges.filter(val => badges.includes(val));
  itemsRepBadges = itemsRepBadges.filter(val => badges.includes(val));
  killsBadges = killsBadges.filter(val => badges.includes(val));
  locksBadges = locksBadges.filter(val => badges.includes(val));
  petsBadges = petsBadges.filter(val => badges.includes(val));
  pillsBadges = pillsBadges.filter(val => badges.includes(val));
  powRemBadges = powRemBadges.filter(val => badges.includes(val));
  powResBadges = powResBadges.filter(val => badges.includes(val));
  targetsBadges = targetsBadges.filter(val => badges.includes(val));
  exploreBadges = exploreBadges.filter(val => badges.includes(val));

  var badgeNumNorm = ["< 10", "10 - 49", "50 - 99", "100 - 499", "500 - 999", "≥ 1000"];
  var badgeNumDam = ["< 500", "500 - 999", "1000 - 4999", "5000 - 9999", "10000 - 49999", "50000 - 99999", "≥ 100000"];
  var badgeNumHeal = ["< 500", "500 - 999", "1000 - 4999", "5000 - 9999", "10000 - 14999", "15000 - 19999", "≥ 20000"];

  document.getElementById('charAlc').innerHTML = badgeNumNorm[alcoholBadges.length];
  document.getElementById('charAngel').innerHTML = badgeNumNorm[angelBadges.length];
  document.getElementById('charBooks').innerHTML = badgeNumNorm[booksBadges.length];
  document.getElementById('charDamDeal').innerHTML = badgeNumDam[damDealBadges.length];
  document.getElementById('charDamTake').innerHTML = badgeNumDam[damTakeBadges.length];
  document.getElementById('charDeaths').innerHTML = badgeNumNorm[deathsBadges.length];
  document.getElementById('charDemons').innerHTML = badgeNumNorm[demonsBadges.length];
  document.getElementById('charDoorsDest').innerHTML = badgeNumNorm[doorsDestBadges.length];
  document.getElementById('charDoorsRep').innerHTML = badgeNumNorm[doorsRepBadges.length];
  document.getElementById('charFood').innerHTML = badgeNumNorm[foodBadges.length];
  document.getElementById('charHp').innerHTML = badgeNumHeal[healBadges.length];
  document.getElementById('charItCraft').innerHTML = badgeNumNorm[itemsCraBadges.length];
  document.getElementById('charItRep').innerHTML = badgeNumNorm[itemsRepBadges.length];
  document.getElementById('charKills').innerHTML = badgeNumNorm[killsBadges.length];
  document.getElementById('charLocks').innerHTML = badgeNumNorm[locksBadges.length];
  document.getElementById('charPets').innerHTML = badgeNumNorm[petsBadges.length];
  document.getElementById('charPills').innerHTML = badgeNumNorm[pillsBadges.length];
  document.getElementById('charPowerRem').innerHTML = badgeNumNorm[powRemBadges.length];
  document.getElementById('charPowerRest').innerHTML = badgeNumNorm[powResBadges.length];
  document.getElementById('charTargets').innerHTML = badgeNumNorm[targetsBadges.length];

  if (exploreBadges.length == 0) {
    document.getElementById('exploreBadges').innerHTML = name + " has not found any exploration badges yet<p> 40 badges left to find";
  } else {
    badgesLeft = 40 - exploreBadges.length;
    document.getElementById('exploreBadges').innerHTML = "Exploration Badges obtained: <p>" + exploreBadges + "<p>" + badgesLeft + " badges left to find";
  }
}

async function getData2(corsUrl) {
    const response = await fetch(corsUrl, {});
    const json = await response.json();

    return json;
}
