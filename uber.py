def getUberDeepLink(destLat, destLong):
    deeplink = "uber://?client_id=sTL8jQXWMhI5aMuMggq7YAVqqJh5_vECD&action=setPickup&pickup=my_location&pickup[nickname]=FacebHQ&dropoff[latitude]="
    deeplink = deeplink + str(destLat) + "&dropoff[longitude]=" + str(destLong) + "dropoff[nickname]=GoingSomewhere"
    
    return deeplink
