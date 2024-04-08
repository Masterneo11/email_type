class Email:
    
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError("Hey try a str ")
        if "@" not in content:
            raise TypeError("does not have a "@" sign")
    
        # ends with .com . edu .net
        # tld = top level domain , which is the com/org/net
        valid_tlds: list[str] = [".com", ".edu",".net",".org"]
        tld = content[-4:]
        if tld not in valid_tlds:
                raise TypeError("invalid .com thing ending")
    
        # check for domain (stuff between @ and .com)
        at_sign_index = content.index("@")
        domain = content[at_sign_index+1:-4]
        if domain == "":
            raise TypeError("invalid domain like gmail or yahoo")
        
        if content.find("@") == 0:
            raise TypeError("invalid user")
        self.content = content

        def __str__(self) -> str:
            return self.content

