#!/usr/bin/env python

from heuristic import PyQemuHeuristic

crypt_api_calls = [
	"ExitProcess",
	"ExitThread",
	"CertAddCertificateContextToStore",
	"CertAddCertificateLinkToStore",
	"CertAddCRLContextToStore",
	"CertAddCRLLinkToStore",
	"CertAddCTLContextToStore",
	"CertAddCTLLinkToStore",
	"CertAddEncodedCertificateToStore",
	"CertAddEncodedCertificateToSystemStoreA",
	"CertAddEncodedCertificateToSystemStoreW",
	"CertAddEncodedCRLToStore",
	"CertAddEncodedCTLToStore",
	"CertAddEnhancedKeyUsageIdentifier",
	"CertAddRefServerOcspResponse",
	"CertAddRefServerOcspResponseContext",
	"CertAddSerializedElementToStore",
	"CertAddStoreToCollection",
	"CertAlgIdToOID",
	"CertCloseServerOcspResponse",
	"CertCloseStore",
	"CertCompareCertificate",
	"CertCompareCertificateName",
	"CertCompareIntegerBlob",
	"CertComparePublicKeyInfo",
	"CertControlStore",
	"CertCreateCertificateChainEngine ",
	"CertCreateCertificateContext",
	"CertCreateContext",
	"CertCreateCRLContext",
	"CertCreateCTLContext",
	"CertCreateCTLEntryFromCertificateContextProperties",
	"CertCreateSelfSignCertificate",
	"CertDeleteCertificateFromStore",
	"CertDeleteCRLFromStore",
	"CertDeleteCTLFromStore",
	"CertDuplicateCertificateChain ",
	"CertDuplicateCertificateContext",
	"CertDuplicateCRLContext",
	"CertDuplicateCTLContext",
	"CertDuplicateStore",
	"CertEnumCertificateContextProperties",
	"CertEnumCertificatesInStore",
	"CertEnumCRLContextProperties",
	"CertEnumCRLsInStore",
	"CertEnumCTLContextProperties",
	"CertEnumCTLsInStore",
	"CertEnumPhysicalStore",
	"CertEnumSubjectInSortedCTL",
	"CertEnumSystemStore",
	"CertEnumSystemStoreLocation",
	"CertFindAttribute",
	"CertFindCertificateInCRL",
	"CertFindCertificateInStore",
	"CertFindChainInStore",
	"CertFindCRLInStore",
	"CertFindCTLInStore",
	"CertFindExtension",
	"CertFindRDNAttr",
	"CertFindSubjectInCTL",
	"CertFindSubjectInSortedCTL",
	"CertFreeCertificateChain ",
	"CertFreeCertificateChainEngine ",
	"CertFreeCertificateChainList",
	"CertFreeCertificateContext",
	"CertFreeCRLContext",
	"CertFreeCTLContext",
	"CertFreeServerOcspResponseContext",
	"CertGetCertificateChain ",
	"CertGetCertificateContextProperty",
	"CertGetCRLContextProperty",
	"CertGetCRLFromStore",
	"CertGetCTLContextProperty",
	"CertGetEnhancedKeyUsage",
	"CertGetIntendedKeyUsage",
	"CertGetIssuerCertificateFromStore",
	"CertGetNameStringA",
	"CertGetNameStringW",
	"CertGetPublicKeyLength",
	"CertGetServerOcspResponseContext",
	"CertGetStoreProperty",
	"CertGetSubjectCertificateFromStore",
	"CertGetValidUsages",
	"CertIsRDNAttrsInCertificateName",
	"CertIsValidCRLForCertificate",
	"CertNameToStrA",
	"CertNameToStrW",
	"CertOIDToAlgId",
	"CertOpenServerOcspResponse",
	"CertOpenStore",
	"CertOpenSystemStoreA",
	"CertOpenSystemStoreW",
	"CertRDNValueToStrA",
	"CertRDNValueToStrW",
	"CertRegisterPhysicalStore",
	"CertRegisterSystemStore",
	"CertRemoveEnhancedKeyUsageIdentifier",
	"CertRemoveStoreFromCollection",
	"CertResyncCertificateChainEngine ",
	"CertRetrieveLogoOrBiometricInfo",
	"CertSaveStore",
	"CertSelectCertificateChains",
	"CertSerializeCertificateStoreElement",
	"CertSerializeCRLStoreElement",
	"CertSerializeCTLStoreElement",
	"CertSetCertificateContextPropertiesFromCTLEntry",
	"CertSetCertificateContextProperty",
	"CertSetCRLContextProperty",
	"CertSetCTLContextProperty",
	"CertSetEnhancedKeyUsage",
	"CertSetStoreProperty",
	"CertStrToNameA",
	"CertStrToNameW",
	"CertUnregisterPhysicalStore",
	"CertUnregisterSystemStore",
	"CertVerifyCertificateChainPolicy",
	"CertVerifyCRLRevocation",
	"CertVerifyCRLTimeValidity",
	"CertVerifyCTLUsage",
	"CertVerifyRevocation",
	"CertVerifySubjectCertificateContext",
	"CertVerifyTimeValidity",
	"CertVerifyValidityNesting",
	"CryptAcquireCertificatePrivateKey",
	"CryptAcquireContextA",
	"CryptAcquireContextW",
	"CryptBinaryToStringA",
	"CryptBinaryToStringW",
	"CryptCancelAsyncRetrieval ",
	"CryptCloseAsyncHandle ",
	"CryptContextAddRef",
	"CryptCreateAsyncHandle ",
	"CryptCreateHash",
	"CryptCreateKeyIdentifierFromCSP",
	"CryptDecodeMessage",
	"CryptDecodeObject",
	"CryptDecodeObjectEx",
	"CryptDecrypt",
	"CryptDecryptAndVerifyMessageSignature",
	"CryptDecryptMessage",
	"CryptDeriveKey",
	"CryptDestroyHash",
	"CryptDestroyKey",
	"CryptDuplicateHash",
	"CryptDuplicateKey",
	"CryptEncodeObject",
	"CryptEncodeObjectEx",
	"CryptEncrypt",
	"CryptEncryptMessage",
	"CryptEnumKeyIdentifierProperties",
	"CryptEnumOIDFunction",
	"CryptEnumOIDInfo",
	"CryptEnumProvidersA",
	"CryptEnumProvidersW",
	"CryptEnumProviderTypesA",
	"CryptEnumProviderTypesW",
	"CryptExportKey",
	"CryptExportPKCS8",
	"CryptExportPKCS8Ex",
	"CryptExportPublicKeyInfo",
	"CryptExportPublicKeyInfoEx",
	"CryptExportPublicKeyInfoFromBCryptKeyHandle",
	"CryptFindCertificateKeyProvInfo",
	"CryptFindLocalizedName",
	"CryptFindOIDInfo",
	"CryptFlushTimeValidObject ",
	"CryptFormatObject",
	"CryptFreeOIDFunctionAddress",
	"CryptGenKey",
	"CryptGenRandom",
	"CryptGetAsyncParam ",
	"CryptGetDefaultOIDDllList",
	"CryptGetDefaultOIDFunctionAddress",
	"CryptGetDefaultProviderA",
	"CryptGetDefaultProviderW",
	"CryptGetHashParam",
	"CryptGetKeyIdentifierProperty",
	"CryptGetKeyParam",
	"CryptGetMessageCertificates",
	"CryptGetMessageSignerCount",
	"CryptGetObjectUrl ",
	"CryptGetOIDFunctionAddress",
	"CryptGetOIDFunctionValue",
	"CryptGetProvParam",
	"CryptGetTimeValidObject ",
	"CryptGetUserKey",
	"CryptHashCertificate",
	"CryptHashCertificate2",
	"CryptHashData",
	"CryptHashMessage",
	"CryptHashPublicKeyInfo",
	"CryptHashSessionKey",
	"CryptHashToBeSigned",
	"CryptImportKey",
	"CryptImportPKCS8",
	"CryptImportPublicKeyInfo",
	"CryptImportPublicKeyInfoEx",
	"CryptImportPublicKeyInfoEx2",
	"CryptInitOIDFunctionSet",
	"CryptInstallCancelRetrieval",
	"CryptInstallDefaultContext",
	"CryptInstallOIDFunctionAddress",
	"CryptMemAlloc ",
	"CryptMemFree ",
	"CryptMemRealloc ",
	"CryptMsgCalculateEncodedLength",
	"CryptMsgClose",
	"CryptMsgControl",
	"CryptMsgCountersign",
	"CryptMsgCountersignEncoded",
	"CryptMsgDuplicate",
	"CryptMsgEncodeAndSignCTL",
	"CryptMsgGetAndVerifySigner",
	"CryptMsgGetParam",
	"CryptMsgOpenToDecode",
	"CryptMsgOpenToEncode",
	"CryptMsgSignCTL",
	"CryptMsgUpdate",
	"CryptMsgVerifyCountersignatureEncoded",
	"CryptMsgVerifyCountersignatureEncodedEx",
	"CryptProtectData",
	"CryptProtectMemory",
	"CryptQueryObject",
	"CryptRegisterDefaultOIDFunction",
	"CryptRegisterOIDFunction",
	"CryptRegisterOIDInfo",
	"CryptReleaseContext",
	"CryptRetrieveObjectByUrlA ",
	"CryptRetrieveObjectByUrlW ",
	"CryptRetrieveTimeStamp",
	"CryptSetAsyncParam ",
	"CryptSetHashParam",
	"CryptSetKeyIdentifierProperty",
	"CryptSetKeyParam",
	"CryptSetOIDFunctionValue",
	"CryptSetProviderA",
	"CryptSetProviderExA",
	"CryptSetProviderExW",
	"CryptSetProviderW",
	"CryptSetProvParam",
	"CryptSignAndEncodeCertificate",
	"CryptSignAndEncryptMessage",
	"CryptSignCertificate",
	"CryptSignHashA",
	"CryptSignHashW",
	"CryptSignMessage",
	"CryptSignMessageWithKey",
	"CryptStringToBinaryA",
	"CryptStringToBinaryW",
	"CryptUninstallCancelRetrieval",
	"CryptUninstallDefaultContext",
	"CryptUnprotectData",
	"CryptUnprotectMemory",
	"CryptUnregisterDefaultOIDFunction",
	"CryptUnregisterOIDFunction",
	"CryptUnregisterOIDInfo",
	"CryptUpdateProtectedState",
	"CryptVerifyCertificateSignature",
	"CryptVerifyCertificateSignatureEx",
	"CryptVerifyDetachedMessageHash",
	"CryptVerifyDetachedMessageSignature",
	"CryptVerifyMessageHash",
	"CryptVerifyMessageSignature",
	"CryptVerifyMessageSignatureWithKey",
	"CryptVerifySignatureA",
	"CryptVerifyTimeStampSignature",
	"CryptVerifySignatureW",
]

class ApiHeuristic(PyQemuHeuristic):
	PREFIX = "ApiCall"

	def setupCallbacks(self):
		self.process.onInstrumentationInit(lambda: self.registerApiHooks(self.process))
		self.process.onInstrumentationInit(lambda: self.process.hardware.instrumentation.bblwindow_enable(100))

	def registerApiHooks(self, process):
		for function in crypt_api_calls:
			process.installHookByName(self.onApiCallEvent, function)

	def onApiCallEvent(self, process, dll, function, addr):
		last_bbls = []
		for i in range(3):
			last_bbls.append(process.hardware.instrumentation.bblwindow_get(i))
		self.log("%s(%s,%s, 0x%x->0x%x->0x%x)"%(self.PREFIX, dll, function, last_bbls[2], last_bbls[1], last_bbls[0]))

heuristic = ApiHeuristic
