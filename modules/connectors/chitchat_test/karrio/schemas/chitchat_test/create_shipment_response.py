from attr import s
from typing import Optional, Any, List
from jstruct import JList, JStruct


@s(auto_attribs=True)
class RateType:
    postagetype: Optional[str] = None
    postagecarriertype: Optional[str] = None
    postagedescription: Optional[str] = None
    signatureconfirmationdescription: Any = None
    deliverydutiespaiddescription: Any = None
    deliverytimedescription: Optional[str] = None
    trackingtypedescription: Optional[str] = None
    isinsured: Optional[bool] = None
    purchaseamount: Optional[str] = None
    provincialtax: Any = None
    provincialtaxlabel: Any = None
    federaltax: Optional[str] = None
    federaltaxlabel: Optional[str] = None
    postagefee: Optional[str] = None
    insurancefee: Optional[str] = None
    deliveryfee: Any = None
    paymentamount: Optional[str] = None


@s(auto_attribs=True)
class TrackingEventType:
    type: Optional[str] = None
    title: Optional[str] = None
    subtitle: Any = None
    locationdescription: Any = None
    createdat: Optional[str] = None
    status: Any = None


@s(auto_attribs=True)
class ShipmentType:
    id: Optional[str] = None
    status: Optional[str] = None
    batchid: Any = None
    toname: Optional[str] = None
    toaddress1: Optional[str] = None
    toaddress2: Any = None
    tocity: Optional[str] = None
    toprovincecode: Optional[str] = None
    topostalcode: Optional[str] = None
    tocountrycode: Optional[str] = None
    tophone: Optional[str] = None
    toemail: Any = None
    returnname: Any = None
    returnaddress1: Any = None
    returnaddress2: Any = None
    returncity: Any = None
    returnprovincecode: Any = None
    returnpostalcode: Any = None
    returncountrycode: Any = None
    returnphone: Any = None
    isreturndispose: Optional[bool] = None
    packagecontents: Optional[str] = None
    description: Optional[str] = None
    value: Optional[str] = None
    valuecurrency: Optional[str] = None
    orderid: Any = None
    orderstore: Any = None
    packagetype: Optional[str] = None
    sizeunit: Optional[str] = None
    sizex: Optional[float] = None
    sizey: Optional[float] = None
    sizez: Optional[float] = None
    weightunit: Optional[str] = None
    weight: Optional[float] = None
    isinsured: Optional[bool] = None
    isinsurancerequested: Optional[bool] = None
    ismediamailrequested: Optional[bool] = None
    issignaturerequested: Optional[bool] = None
    isdeliverydutiespaidrequested: Optional[bool] = None
    postagetype: Optional[str] = None
    carrier: Optional[str] = None
    carriertrackingcode: Any = None
    trackingurl: Optional[str] = None
    shipdate: Optional[str] = None
    purchaseamount: Optional[str] = None
    provincialtax: Any = None
    provincialtaxlabel: Any = None
    federaltax: Optional[str] = None
    federaltaxlabel: Optional[str] = None
    postagefee: Optional[str] = None
    insurancefee: Optional[str] = None
    deliveryfee: Any = None
    createdat: Optional[str] = None
    postagelabelpngurl: Any = None
    postagelabelzplurl: Any = None
    rates: List[RateType] = JList[RateType]
    trackingevents: List[TrackingEventType] = JList[TrackingEventType]


@s(auto_attribs=True)
class CreateShipmentResponseType:
    shipment: Optional[ShipmentType] = JStruct[ShipmentType]
