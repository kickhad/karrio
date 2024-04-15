from attr import s
from typing import Optional, Any


@s(auto_attribs=True)
class CreateShipmentRequestType:
    name: Optional[str] = None
    address1: Optional[str] = None
    address2: Any = None
    city: Optional[str] = None
    provincecode: Optional[str] = None
    postalcode: Optional[str] = None
    countrycode: Optional[str] = None
    phone: Optional[str] = None
    email: Any = None
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
    insurancefee: Any = None
    deliveryfee: Any = None
    createdat: Optional[str] = None
    postagelabelpngurl: Any = None
    postagelabelzplurl: Any = None
