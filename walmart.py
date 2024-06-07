import requests
import json

url = "https://www.walmart.ca/orchestra/graphql/browse?page=1&prg=desktop&catId=10019_6000194327370&sort=best_match&ps=40&limit=40&additionalQueryParams.isMoreOptionsTileEnabled=true&additionalQueryParams.isGenAiEnabled=undefined&additionalQueryParams.view_module=undefined&searchArgs.cat_id=10019_6000194327370&searchArgs.prg=desktop&fitmentFieldParams=true_true_false&enableFashionTopNav=false&fetchMarquee=true&fetchSkyline=true&fetchSbaTop=false&fetchGallery=false&fetchDac=false&enablePortableFacets=true&tenant=CA_GLASS&pageType=BrowsePage&enableFacetCount=true&marketSpecificParams=\\{%22pageType%22:%22browse%22\\}&enableFlattenedFitment=false&enableMultiSave=true&fSeo=true&enableSellerType=true&enableFulfillmentTagsEnhacements=false"

payload = "{\"query\":\"query Browse( $query:String $limit:Int $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $pap:String $ps:Int $ptss:String $beShelfId:String $fitmentFieldParams:JSON ={}$fitmentSearchParams:JSON ={}$rawFacet:String $seoPath:String $trsp:String $fetchMarquee:Boolean! $fetchSkyline:Boolean! $fetchGallery:Boolean! $fetchSbaTop:Boolean! $fetchDac:Boolean! $additionalQueryParams:JSON ={}$enablePortableFacets:Boolean = false $enableFashionTopNav:Boolean = false $intentSource:IntentSource $tenant:String! $enableFacetCount:Boolean = true $pageType:String! = \\\"BrowsePage\\\" $marketSpecificParams:String $enableFlattenedFitment:Boolean = false $enableMultiSave:Boolean = false $fSeo:Boolean = true $enableSellerType:Boolean = false $enableAdditionalSearchDepartmentAnalytics:Boolean = false $enableFulfillmentTagsEnhacements:Boolean = false $disableAds:Boolean = false ){search( query:$query limit:$limit page:$page prg:$prg pap:$pap facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp intentSource:$intentSource _be_shelf_id:$beShelfId pageType:$pageType ){query searchResult{...BrowseResultFragment}}contentLayout( channel:\\\"WWW\\\" pageType:$pageType tenant:$tenant version:\\\"v1\\\" searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules( p13n:{page:$page userReqInfo:{refererContext:{catId:$catId}}}){...ModuleFragment configs{__typename...on EnricherModuleConfigsV1{zoneV1}...on TempoWM_GLASSWWWEmailSignUpWidgetConfigs{_rawConfigs}...on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1 @skip(if:$enablePortableFacets){...GenericFacetFragment}topNavFacets @include(if:$enablePortableFacets){...GenericFacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...GenericFacetFragment}}...on TempoWM_GLASSWWWPillsModuleConfigs{moduleSource pillsV2{...GenericPillsModuleFragment}}...TileTakeOverProductFragment...on TempoWM_GLASSWWWSearchFitmentModuleConfigs{fitments( fitmentSearchParams:$fitmentSearchParams fitmentFieldParams:$fitmentFieldParams ){...FitmentFragment sisFitmentResponse{...BrowseResultFragment}}}...on TempoWM_GLASSWWWSearchACCStoreSelectionConfigs{ctaText userInfoMessage headingDetails{heading headingWhenFulfillmentIsSelectedAsPickup}}...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWSponsoredProductCarouselConfigs{_rawConfigs}...on TempoWM_GLASSWWWBenefitProgramBannerPlaceholderConfigs{_rawConfigs}...on TempoWM_GLASSWWWBrowseRelatedShelves @include(if:$fSeo){seoBrowseRelmData( id:$catId marketSpecificParams:$marketSpecificParams ){relm{id url name}}}...FashionTopNavFragment @include(if:$enableFashionTopNav)...BrandAmplifierAdConfigs @include(if:$fetchSbaTop)...PopularInModuleFragment...CopyBlockModuleFragment...BannerModuleFragment...HeroPOVModuleFragment...InlineSearchModuleFragment...MarqueeDisplayAdConfigsFragment @include(if:$fetchMarquee)...SkylineDisplayAdConfigsFragment @include(if:$fetchSkyline)...GalleryDisplayAdConfigsFragment @include(if:$fetchGallery)...DynamicAdContainerConfigsFragment @include(if:$fetchDac)...HorizontalChipModuleConfigsFragment...SkinnyBannerFragment...GenericSeoFaqFragment...SponsoredVideoAdFragment}}...LayoutFragment pageMetadata{location{pickupStore deliveryStore intent postalCode stateOrProvinceCode city storeId accessPointId accessType spokeNodeId}pageContext}}seoBrowseMetaData( id:$catId facets:$rawFacet path:$seoPath facet_query_param:$facet _be_shelf_id:$beShelfId marketSpecificParams:$marketSpecificParams ){metaTitle metaDesc metaCanon h1 noIndex}}fragment BrowseResultFragment on SearchInterface{title aggregatedCount...GenericBreadCrumbFragment...ShelfDataFragment...GenericDebugFragment...GenericItemStacksFragment...GenericPageMetaDataFragment...GenericPaginationFragment...GenericRequestContextFragment...GenericErrorResponse modules{facetsV1 @skip(if:$enablePortableFacets){...GenericFacetFragment}topNavFacets @include(if:$enablePortableFacets){...GenericFacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...GenericFacetFragment}pills{...GenericPillsModuleFragment}}pac{relevantPT{productType score}showPAC reasonCode}}fragment ModuleFragment on TempoModule{__typename type name version moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment GenericBreadCrumbFragment on SearchInterface{breadCrumb{id name url cat_level}}fragment ShelfDataFragment on SearchInterface{shelfData{shelfName shelfId}}fragment GenericDebugFragment on SearchInterface{debug{sisUrl adsUrl genAIDebugInfo{searchAlgorithm isGenAiQueryEligible genAIUnavailableReason reformulatedQuery}presoDebugInformation{explainerToolsResponse}}}fragment GenericItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{adsBeacon{adUuid moduleInfo max_ads}spBeaconInfo{adUuid moduleInfo pageViewUUID placement max}query isPartialResult stackId stackType stackName title description subTitle titleKey queryUsedForSearchResults layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set groupIdentifier min_price max_price view_module shouldHide buttonTitle}borderColor iconUrl}itemsV2{...GenericItemFragment...GenericInGridMarqueeAdFragment @skip(if:$disableAds)...GenericInGridAdFragment @skip(if:$disableAds)...GenericTileTakeOverTileFragment}content{title subtitle data{type name displayName url imageUrl}}}}fragment GenericItemFragment on Product{__typename buyBoxSuppression similarItems id usItemId wfsEnabled @include(if:$enableSellerType) fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription weightIncrement topResult additionalOfferCount availabilityInNearbyStore imageInfo{...GenericProductImageInfoFragment}aspectInfo{name header id snippet}canonicalUrl externalInfo{url}itemType category{categoryPathId path{name url}}returnPolicy{returnable freeReturns returnWindow{value unitType}returnPolicyText}discounts{...GenericProductDiscountsFragment}badges{flags{__typename...on BaseBadge{key bundleId @include(if:$enableMultiSave) text type id styleId}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{key text type}}groups{__typename name members{...on BadgeGroupMember{__typename id key memberType otherInfo{moqText}rank slaText styleId text type iconId templates{regular faster unavailable}badgeContent{type value id}}...on CompositeGroupMember{__typename join memberType styleId suffix members{__typename id key memberType rank slaText styleId text type iconId}}}}}buyNowEligible classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName hasSellerBadge isEarlyAccessItem preEarlyAccessEvent earlyAccessEvent blitzItem annualEvent annualEventV2 availabilityStatusV2{display value}groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId offerType @include(if:$enableFulfillmentTagsEnhacements) preOrder{...GenericPreorderFragment}pac{showPAC reasonCode fulfillmentPacModule}fulfillmentSummary{storeId deliveryDate}priceInfo{...GenericProductPriceInfoFragment}variantCriteria{...GenericVariantCriteriaFragment}snapEligible fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags viewBeacon}showOptions showBuyNow quickShop quickShopCTALabel rewards{eligible state minQuantity rewardAmt promotionId selectionToken rewardMultiplierStr cbOffer term expiry description}promoDiscount{discount discountEligible discountEligibleVariantPresent promotionId promoOffer state showOtherEligibleItemsCTA type min awardValue}arExperiences{isARHome isZeekit isAROptical}eventAttributes{...GenericProductEventAttributesFragment}subscription{subscriptionEligible}hasCarePlans petRx{eligible singleDispense}vision{ageGroup visionCenterApproved}showExploreOtherConditionsCTA isPreowned pglsCondition newConditionProductId preownedCondition keyAttributes{displayEnum value}mhmdFlag seeSimilar subscription{subscriptionEligible showSubscriptionCTA}}fragment GenericProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice priceString}currentPrice{...GenericProductPriceFragment priceDisplay}comparisonPrice{...GenericProductPriceFragment}wasPrice{...GenericProductPriceFragment}unitPrice{...GenericProductPriceFragment}listPrice{...GenericProductPriceFragment}savingsAmount{...GenericProductSavingsFragment}shipPrice{...GenericProductPriceFragment}subscriptionPrice{priceString subscriptionString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType isB2BPrice}wPlusEarlyAccessPrice{memberPrice{...GenericProductPriceFragment}savings{...GenericProductSavingsFragment}eventStartTime eventStartTimeDisplay}subscriptionDualPrice subscriptionPercentage}fragment GenericProductSavingsFragment on ProductSavings{amount percent priceString}fragment GenericProductPriceFragment on ProductPrice{price priceString variantPriceString priceType currencyUnit priceDisplay}fragment GenericProductEventAttributesFragment on EventAttributes{priceFlip specialBuy}fragment GenericPreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage streetDate streetDateDisplayable streetDateType releaseDate}fragment GenericVariantCriteriaFragment on VariantCriterion{name type id displayName isVariantTypeSwatch variantList{id images name rank swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment GenericProductDiscountsFragment on Discounts{discountedValue{price priceString}discountMetaData{id type savings{amount priceString percent}price{price priceString priceDisplay}unitPrice{price priceString}comparisonPrice{price priceString}unitPriceDisplayCondition}}fragment GenericProductImageInfoFragment on ProductImageInfo{id name thumbnailUrl size}fragment GenericInGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment GenericInGridAdFragment on AdPlaceholder{__typename type moduleLocation lazy adUuid hasVideo moduleInfo}fragment GenericTileTakeOverTileFragment on TileTakeOverProductPlaceholder{__typename type tileTakeOverTile{span title subtitle image{src alt assetId assetName}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}adsEnabled adCardLocation enableLazyLoad}}fragment GenericPageMetaDataFragment on SearchInterface{pageMetadata{storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical source description location{addressId}subscriptionEligible}}fragment GenericPaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment GenericRequestContextFragment on SearchInterface{requestContext{vertical hasGicIntent isFitmentFilterQueryApplied searchMatchType categories{id name}}}fragment GenericErrorResponse on SearchInterface{errorResponse{correlationId source errorCodes errors{errorType statusCode statusMsg source}}}fragment GenericPillsModuleFragment on PillsSearchInterface{title titleColor url image:imageV1{src alt assetId assetName}}fragment BannerViewConfigFragment on BannerViewConfigCLS{title image imageAlt displayName description url urlAlt appStoreLink appStoreLinkAlt playStoreLink playStoreLinkAlt}fragment BannerModuleFragment on TempoWM_GLASSWWWSearchBannerConfigs{moduleType viewConfig{...BannerViewConfigFragment}}fragment PopularInModuleFragment on TempoWM_GLASSWWWPopularInBrowseConfigs{seoBrowseRelmData(id:$catId){relm{id name url}}}fragment CopyBlockModuleFragment on TempoWM_GLASSWWWCopyBlockConfigs{copyBlock(id:$catId marketSpecificParams:$marketSpecificParams){cwc}}fragment GenericFacetFragment on Facet{title name expandOnLoad type displayType layout min max selectedMin selectedMax unboundedMax stepSize isSelected values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL catPathName @include(if:$enableAdditionalSearchDepartmentAnalytics) values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL values{id title name expandOnLoad description type itemCount @include(if:$enableFacetCount) isSelected baseSeoURL}}}}}}}}}fragment FitmentFragment on Fitments{partTypeIDs fitmentType isNarrowSearch fitmentOptionalFields{...FitmentFieldFragment}result{fitmentType status formId position quantityTitle extendedAttributes{...FitmentFieldFragment}labels{...LabelFragment}resultSubTitle notes suggestions{...FitmentSuggestionFragment}oilChangeSchedulingInfo{formattedOilViscosity oilViscosity oilViscosityLabel formattedOilType oilType oilTypeLabel formattedOilCapacity oilCapacityQuarts oilCapacityLabel fittingOilFilters{brand manufacturerNumber}}}redirectUrl{title clickThrough{value}}labels{...LabelFragment}savedVehicle{vehicleType{...VehicleFieldFragment}vehicleYear{...VehicleFieldFragment}vehicleMake{...VehicleFieldFragment}vehicleModel{...VehicleFieldFragment}additionalAttributes{...VehicleFieldFragment}}fitmentFields{...VehicleFieldFragment}fitmentForms{id fields{...FitmentFieldFragment}title labels{...LabelFragment}garage{vehicles{...AutoVehicle}}}}fragment LabelFragment on FitmentLabels{ctas{...FitmentLabelEntityFragment}messages{...FitmentLabelEntityFragment}links{...FitmentLabelEntityFragment}images{...FitmentLabelEntityFragment}}fragment FitmentLabelEntityFragment on FitmentLabelEntity{id label labelV1 @include(if:$enableFlattenedFitment)}fragment VehicleFieldFragment on FitmentVehicleField{id label value}fragment FitmentFieldFragment on FitmentField{id displayName value extended data{value label}dependsOn isRequired errorMessage}fragment FitmentSuggestionFragment on FitmentSuggestion{id position loadIndex speedRating searchQueryParam labels{...LabelFragment}cat_id fitmentSuggestionParams{id value}optionalSuggestionParams{id value displayName data{label value}dependsOn isRequired errorMessage}applicationSuggestionParams{position}}fragment HeroPOVModuleFragment on TempoWM_GLASSWWWHeroPovConfigsV1{povCards{card:cardV1{povStyle image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}heading{text textColor textSize}subheading{text textColor}detailsView{backgroundColor isTransparent alignment}ctaButton{button{linkText clickThrough{value}uid}ctaButtonBackgroundColor textColor}legalDisclosure{regularText shortenedText textColor textColorMobile legalBottomSheetTitle legalBottomSheetDescription}logo{...TempoCommonImageFragment}links{link{...TempoCommonLinkFragment}textColor textColorMobile}}}}fragment TempoCommonImageFragment on TempoCommonImage{src alt assetId uid clickThrough{value}}fragment TempoCommonLinkFragment on TempoCommonStringLink{linkText title uid clickThrough{value}}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText}fragment MarqueeDisplayAdConfigsFragment on TempoWM_GLASSWWWMarqueeDisplayAdConfigs{_rawConfigs ad{...DisplayAdFragment}}fragment DisplayAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataDisplayAdFragment}}}fragment AdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment SkylineDisplayAdConfigsFragment on TempoWM_GLASSWWWSkylineDisplayAdConfigs{_rawConfigs ad{...SkylineDisplayAdFragment}}fragment SkylineDisplayAdFragment on Ad{...SkylineAdFragment adContent{type data{__typename...SkylineAdDataDisplayAdFragment}}}fragment SkylineAdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment SkylineAdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment GalleryDisplayAdConfigsFragment on TempoWM_GLASSWWWGalleryDisplayAdConfigs{_rawConfigs}fragment DynamicAdContainerConfigsFragment on TempoWM_GLASSWWWDynamicAdContainerConfigs{_rawConfigs adModules{moduleType moduleLocation priority adServers{adServer}}zoneLocation lazy}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource heading headingColor backgroundImage{src alt}backgroundColor desktopImageHeight desktopImageWidth mobileImageHeight mobileImageWidth chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title titleColor url{linkText title clickThrough{type value}}image{assetId assetName alt clickThrough{type value}height src title width}}}fragment SkinnyBannerFragment on TempoWM_GLASSWWWSkinnyBannerConfigs{campaignsV1{bannerType desktopBannerHeight bannerImage{src title alt assetId assetName}mobileBannerHeight mobileImage{src title alt assetId assetName}clickThroughUrl{clickThrough{value}}backgroundColor heading{title fontColor}subHeading{title fontColor}bannerCta{ctaLink{linkText clickThrough{value}}textColor ctaType}}}fragment TileTakeOverProductFragment on TempoWM_GLASSWWWTileTakeOverProductConfigs{dwebSlots mwebSlots overrideDefaultTiles TileTakeOverProductDetailsV1{pageNumber span dwebPosition mwebPosition title subtitle image{src alt assetId assetName}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title uid}ctaType ctaTextColor}adsEnabled adCardLocation enableLazyLoad}}fragment FashionTopNavFragment on TempoWM_GLASSWWWCategoryTopNavConfigs{navHeaders{header{linkText clickThrough{value}}headerImageGroup{headerImage{alt src assetId assetName}imgTitle imgSubText imgLink{linkText title clickThrough{value}}}categoryGroup{category{linkText clickThrough{value}}startNewColumn subCategoryGroup{subCategory{linkText clickThrough{value}}isBold openInNewTab}}}}fragment BrandAmplifierAdConfigs on TempoWM_GLASSWWWBrandAmplifierAdConfigs{_rawConfigs moduleLocation ad{...SponsoredBrandsAdFragment}}fragment SponsoredBrandsAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataSponsoredBrandsFragment}}}fragment AdDataSponsoredBrandsFragment on AdData{...on SponsoredBrands{adUuid adExpInfo moduleInfo brands{logo{featuredHeadline featuredImage featuredImageName featuredUrl logoClickTrackUrl}products{...ProductFragment}}}}fragment ProductFragment on Product{usItemId offerId badges{flags{__typename...on BaseBadge{id text key query type styleId}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought criteria{name value}}}labels{__typename...on BaseBadge{id text key}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{id text key}}groups{__typename name members{...on BadgeGroupMember{__typename id key memberType rank slaText styleId text type}...on CompositeGroupMember{__typename join memberType styleId suffix members{__typename id key memberType rank slaText styleId text type}}}}}priceInfo{priceDisplayCodes{rollback reducedPrice eligibleForAssociateDiscount clearance strikethrough submapType priceDisplayCondition unitOfMeasure pricePerUnitUom}currentPrice{price priceString priceDisplay}wasPrice{price priceString}listPrice{price priceString}priceRange{minPrice maxPrice priceString}unitPrice{price priceString}savingsAmount{priceString}comparisonPrice{priceString}subscriptionPrice{priceString subscriptionString price minPrice maxPrice intervalFrequency duration percentageRate durationUOM interestUOM}wPlusEarlyAccessPrice{memberPrice{price priceString priceDisplay}savings{amount priceString}eventStartTime eventStartTimeDisplay}}annualEventV2 earlyAccessEvent isEarlyAccessItem eventAttributes{priceFlip specialBuy}snapEligible showOptions sponsoredProduct{spQs clickBeacon spTags}canonicalUrl numberOfReviews averageRating availabilityStatus imageInfo{thumbnailUrl allImages{id url}}name fulfillmentBadge classType type showAtc brand}fragment AutoVehicle on AutoVehicle{cid color default documentType fitment{baseBodyType baseVehicleId driveType{id name}engineOptions{id isSelected label}smartSubModel tireSizeOptions{diameter isCustom isSelected loadIndex positions ratio speedRating tirePressureFront tirePressureRear tireSize width}trim}isDually licensePlate licensePlateState licensePlateStateCode make model reminders{id}source sourceType subModel{subModelId subModelName}subModelOptions{subModelId subModelName}vehicleId vehicleType vin year}fragment GenericSeoFaqFragment on TempoWM_GLASSWWWGenericSEOFAQModuleConfigs{seoFaqList:faqList(id:$catId pageType:$pageType){seoFaqQuestion:questionText seoFaqAnswer:answerParagraphs}}fragment SponsoredVideoAdFragment on TempoWM_GLASSWWWSponsoredVideoAdConfigs{__typename sponsoredVideoAd{ad{adContent{data{...on SponsoredVideos{adUuid hasVideo moduleInfo}}}}}}\",\"variables\":{\"id\":\"\",\"dealsId\":\"\",\"query\":\"\",\"page\":3,\"prg\":\"desktop\",\"catId\":\"10019_6000194327370\",\"facet\":\"\",\"sort\":\"best_match\",\"rawFacet\":\"\",\"seoPath\":\"\",\"ps\":40,\"limit\":40,\"ptss\":\"\",\"trsp\":\"\",\"beShelfId\":\"\",\"recall_set\":\"\",\"module_search\":\"\",\"min_price\":\"\",\"max_price\":\"\",\"storeSlotBooked\":\"\",\"additionalQueryParams\":{\"hidden_facet\":null,\"translation\":null,\"isMoreOptionsTileEnabled\":true},\"searchArgs\":{\"query\":\"\",\"cat_id\":\"10019_6000194327370\",\"prg\":\"desktop\",\"facet\":\"\"},\"fitmentFieldParams\":{\"powerSportEnabled\":true,\"dynamicFitmentEnabled\":true,\"extendedAttributesEnabled\":false},\"fitmentSearchParams\":{\"id\":\"\",\"dealsId\":\"\",\"query\":\"\",\"page\":3,\"prg\":\"desktop\",\"catId\":\"10019_6000194327370\",\"facet\":\"\",\"sort\":\"best_match\",\"rawFacet\":\"\",\"seoPath\":\"\",\"ps\":40,\"limit\":40,\"ptss\":\"\",\"trsp\":\"\",\"beShelfId\":\"\",\"recall_set\":\"\",\"module_search\":\"\",\"min_price\":\"\",\"max_price\":\"\",\"storeSlotBooked\":\"\",\"additionalQueryParams\":{\"hidden_facet\":null,\"translation\":null,\"isMoreOptionsTileEnabled\":true},\"searchArgs\":{\"query\":\"\",\"cat_id\":\"10019_6000194327370\",\"prg\":\"desktop\",\"facet\":\"\"},\"cat_id\":\"10019_6000194327370\",\"_be_shelf_id\":\"\"},\"enableFashionTopNav\":false,\"fetchMarquee\":true,\"fetchSkyline\":true,\"fetchSbaTop\":false,\"fetchGallery\":false,\"fetchDac\":false,\"enablePortableFacets\":true,\"tenant\":\"CA_GLASS\",\"pageType\":\"BrowsePage\",\"enableFacetCount\":true,\"marketSpecificParams\":\"{\\\"pageType\\\":\\\"browse\\\"}\",\"enableFlattenedFitment\":false,\"enableMultiSave\":true,\"fSeo\":true,\"enableSellerType\":true,\"enableFulfillmentTagsEnhacements\":false}}"
headers = {
  'accept': 'application/json',
  'accept-language': 'en-CA',
  'content-type': 'application/json',
  'cookie': 'WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; auth=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; DYN_USER_ID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; ACID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; locDataV3=eyJwaWNrdXBTdG9yZSI6eyJhZGRyZXNzTGluZU9uZSI6Ijk4NTUgQXVzdGluIFJkIiwiY2l0eSI6IkJ1cm5hYnkiLCJzdGF0ZU9yUHJvdmluY2VDb2RlIjoiQkMiLCJjb3VudHJ5Q29kZSI6IkNBIiwicG9zdGFsQ29kZSI6IlYzSiAxTjUiLCJzdG9yZUlkIjoiMzAwOCIsImRpc3BsYXlOYW1lIjoiQlVSTkFCWSwgQlJJVElTSCBDT0xVTUJJQSIsImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0OS4yNDkwMjksImxvbmdpdHVkZSI6LTEyMi44OTU1OTh9LCJhY2Nlc3NQb2ludElkIjoiYmM5YjE0YmEtMjc5Yi00NTZjLTg5MTctZGYwZGJhOTU3MGE2IiwiZnVsZmlsbG1lbnRTdG9yZUlkIjoiMzAwOCIsInByaWNpbmdTdG9yZUlkIjoiMzAwOCIsImZ1bGZpbGxtZW50T3B0aW9uIjoiUElDS1VQIiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifSwic2hpcHBpbmciOnsicG9zdGFsQ29kZSI6IlYzSiAxTjUiLCJjaXR5IjoiQnVybmFieSIsInN0YXRlT3JQcm92aW5jZUNvZGUiOiJCQyIsImNvdW50cnlDb2RlIjoiQ0EiLCJsYXRpdHVkZSI6NDkuMjQ5MDI5LCJsb25naXR1ZGUiOi0xMjIuODk1NTk4LCJpc0dpZnRBZGRyZXNzIjpmYWxzZX0sImludGVudCI6IlBJQ0tVUCIsImlzRXhwbGljaXRJbnRlbnQiOmZhbHNlLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NzE4YTFlZjktMmQ1OC00YmRhLWE3ZGEtZmM2NDYzNWYwZjRhIn0%3D; hasLocData=1; sizeID=s7n1frm118dc4htipakiitd314; vtc=WFkwM9p9B1s0mpEQxyrIOs; walmart.nearestLatLng="49.2635,-122.9331"; userSegment=50-percent; _pxvid=92192a0d-1237-11ef-b150-3fad0c304692; cartId=8f2ea269-89df-4aca-994e-3f549c989e79; _ga=GA1.1.902424607.1715721536; _gcl_au=1.1.1882684070.1715721536; localStoreInfo=eyJwb3N0YWxDb2RlIjoiVjNKMU41IiwibG9jYWxTdG9yZUlkIjoiMzAwOCIsInNlbGVjdGVkU3RvcmVJZCI6IjMwMDgiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkJVUk5BQlksIEJSSVRJU0ggQ09MVU1CSUEiLCJmdWxmaWxsbWVudFN0b3JlSWQiOiIzMDA4IiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifQo=; deliveryCatchment=3008; walmart.nearestPostalCode=V3J1N5; walmart.shippingPostalCode=V3J1N5; defaultNearestStoreId=3008; QuantumMetricUserID=df1b13baeb425052cc274724558675ef; uxcon=enforce=false&p13n=true&ads=true&createdAt=1715721533579&modifiedAt=1715721543894; dimensionData=606; _ga_N1HN887KY7=GS1.1.1715816652.3.0.1715816652.60.0.0; userAppVersion=main-1.144.1-1bcdce2-0523T2122; enableHTTPS=1; ak_bmsc=1E9C22D566450F178350752B5CFB1466~000000000000000000000000000000~YAAQmE3bF7rdD+mPAQAA3Xsc7xi1xSukNS5bdspvWKwAPsRiyQe5NqtyEK43EelCorZ+81LPhk9gcFy1uBon3DOQJ9Mqn0zVuIfPjxkEHp5yyFxRX4JSFZ1CkctKATpjwdQhRE6zDR+oRxdnjFJS3FW8BoX2V3X9PQcYF0FurXQB3c8fSLvegXb4NO8495ez03WVo8wexgScFAmLPjUVZpSDA/bpr7CqJuan/O8ey8pBZzHvuIS6JzhhkBKnuv0VAv03mnXPb1qvwUiVPK1GgHFYFnh/REAy5iRwF5qLcu9pZiWnXgE1z+3UXza8k+Cz+iTE2ZtQrBvkNgiwWsTtHbcvpuoG25OPDJct8F+rq3ELhqelDYgzhDExcO5F4JX8TnhFun9tOKeF; wm_route_based_language=en-CA; utmContent=utm_medium=paid_search&utm_source=google&utm_campaign=always_on&cmpid=SEM_CA_138_5565IROSQN_71700000063386362_58700005664773801&utm_id=SEM_CA_138_5565IROSQN_71700000063386362_58700005664773801&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjwvIWzBhAlEiwAHHWgvcyqy3jz3u_HaxyAkXN15xqoCbPXlrgUVvp8Hz38QUrLsHY9ySBs4hoCqPYQAvD_BwE&gclsrc=aw.ds; bstc=Tq1VGadoE6dGBUBF-w495Y; xpa=26diC|2ccV5|4G26Z|4_row|5qeCE|BQ06w|FC6Rc|FQOC3|HwipV|JRzQo|M4aON|NOu94|Qishr|RZX3G|SMS0l|T3Qaq|X18Qx|acQch|bByzn|cU-uC|cfHP2|crfGA|e_PBT|f8NJH|gGsp-|h-wXP|rpnr6|s368N|wOXM5|z6fT8; exp-ck=26diC12ccV514G26Z14_row15qeCE1BQ06w1FQOC31JRzQo1M4aON1NOu941Qishr1RZX3G1SMS0l1acQch1bByzn1cU-uC1e_PBT1f8NJH1rpnr61s368N1z6fT81; cadpweb=true; _astc=0685be377bfcf4b6ca4710446f162b7b; xpm=1%2B1717703572%2BWFkwM9p9B1s0mpEQxyrIOs~%2B0; pxcts=5dd6edfd-243e-11ef-9ae8-82dbaa730cef; ENV=ak-eus-t1-prod; wmt.c=0; QuantumMetricSessionID=2b8eccca48b8293195a1d5717e655920; _gcl_gs=2.1.k1$i1717703632; _gcl_aw=GCL.1717703636.CjwKCAjwvIWzBhAlEiwAHHWgvcyqy3jz3u_HaxyAkXN15xqoCbPXlrgUVvp8Hz38QUrLsHY9ySBs4hoCqPYQAvD_BwE; _gcl_dc=GCL.1717703636.CjwKCAjwvIWzBhAlEiwAHHWgvcyqy3jz3u_HaxyAkXN15xqoCbPXlrgUVvp8Hz38QUrLsHY9ySBs4hoCqPYQAvD_BwE; adblocked=true; _ga_D2P3FM55BM=GS1.1.1717703573.4.1.1717703967.16.0.997806296; _pxde=58f531397a97e306bac6944d5a98137b5e0baab1956d895d08b1215eeefcdebd:eyJ0aW1lc3RhbXAiOjE3MTc3MDQxNDAxMjh9; seqnum=30; TS010110a1=01112140040f6960cb2c6ebe0e71c6476488b02d87bbbfee684f37212a0f0a97d6269a3c49d6b6e72a243ce4ceab575f5b5eea7380; TS01ea8d4c=01112140040f6960cb2c6ebe0e71c6476488b02d87bbbfee684f37212a0f0a97d6269a3c49d6b6e72a243ce4ceab575f5b5eea7380; TS0180da25=01112140040f6960cb2c6ebe0e71c6476488b02d87bbbfee684f37212a0f0a97d6269a3c49d6b6e72a243ce4ceab575f5b5eea7380; TSe62c5f0d027=08a92aee0cab2000587e9d216b6d44242c780cf2310aa3a2d49ac76687118acd712b9b9562894f9208f487c21b113000ae7335dd40487dbaf6fbffc2a7f4923b93641628ce4f6a28d8969c8b415235358a36a332d8248a319967c15f74dbc87a; bm_sv=B2952E0B03823FF42716BD84BC8E8C4F~YAAQmE3bFyvaFemPAQAAZN8n7xhOIQhWrlwYsakOkKK6m0LqBJmpANECE0P6zxQ4s8sYKD1Mi4kidXQ447pA48IlVq+satwrcggG5TaauBdGih6dALsuqpDWtrguOrcba1FWtXBT7qlsg3xZEM0FrmeQTjuLA08+av8vcvdqfo6itcfYC55fQqLuc9GIbKqS/6DBj/oaARLXgzfEjrWfitxuo6ZAnLdH1DxKyWUA/yZxG7Ni+ysQ5YnkltyNATh4ig==~1; ACID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; TS0180da25=017329b0299a49ee7ea56a5caf610d04c7b7026a4a018c0c09553e910900ea9048e43294941030041505a77ecca1d8895b32159441; TS01ea8d4c=017329b0299a49ee7ea56a5caf610d04c7b7026a4a018c0c09553e910900ea9048e43294941030041505a77ecca1d8895b32159441; bstc=Tq1VGadoE6dGBUBF-w495Y; exp-ck=26diC12ccV514G26Z14_row15qeCE1BQ06w1JRzQo1M4aON1NOu941Qishr1RZX3G1acQch1bByzn1cU-uC1e_PBT1f8NJH1rpnr61s368N1z6fT81; seqnum=31; vtc=WFkwM9p9B1s0mpEQxyrIOs; xpa=26diC|2ccV5|4G26Z|4_row|5qeCE|BQ06w|FC6Rc|HwipV|JRzQo|M4aON|NOu94|Qishr|RZX3G|T3Qaq|X18Qx|acQch|bByzn|cU-uC|cfHP2|crfGA|e_PBT|f8NJH|gGsp-|h-wXP|rpnr6|s368N|wOXM5|z6fT8; xpm=1%2B1717711539%2BWFkwM9p9B1s0mpEQxyrIOs~%2B0; DYN_USER_ID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; TS010110a1=017329b0299a49ee7ea56a5caf610d04c7b7026a4a018c0c09553e910900ea9048e43294941030041505a77ecca1d8895b32159441; TSe62c5f0d027=08fe841b0aab20003710b6a61bd855838a63c0459592973644f0f9dc1fd26b8cf3d04e2aa03a63380886712a62113000b22881390eac915fd5e0185b7ec421786e7b367b4eb8b71eb2cdcd7015ab58876f009a2b30ecd0d4c128d0257a4c2886; WM.USER_STATE=GUEST%7CGuest; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; auth=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; type=GUEST%7CGuest',
  'device_profile_ref_id': '9zprbd5zGd571o6VCvh_-ns2lXzVRIClPB7N',
  'dnt': '1',
  'downlink': '10',
  'dpr': '1.5',
  'origin': 'https://www.walmart.ca',
  'priority': 'u=1, i',
  'referer': 'https://www.walmart.ca/en/browse/grocery/fruits-vegetables/10019_6000194327370?icid=cp_l2_page_grocery_shop_all_22967_EMNZA1CAH7&page=3',
  'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-ba6fdf014e08edae567763e54902c8e0-fbf5ec6d5e3d38b3-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.ca/en/browse/grocery/fruits-vegetables/10019_6000194327370?icid=cp_l2_page_grocery_shop_all_22967_EMNZA1CAH7&page=3',
  'wm_qos.correlation_id': 'fTomGj1HUkLQNeLU1xTBk_WDqlhD-6hoIAip',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-CA',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'fTomGj1HUkLQNeLU1xTBk_WDqlhD-6hoIAip',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.144.1-1bcdce2-0523T2122',
  'x-o-segment': 'oaoh'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
data = json.loads(response.text)
print(data['data'])