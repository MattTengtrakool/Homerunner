
CREATE DATABASE HomeRunnder;
Use HomeRunnder;
CREATE TABLE [dbo].[Person](
	[PersonId]  [int] IDENTITY(1,1) NOT NULL,
	[CorrespSalutationFormat] [varchar](1) NULL,
	[FirstName] [varchar](30) NOT NULL,
	[LastName] [varchar](30) NOT NULL,	
	[PersonType][varchar](30) NOT NULL,
	[Address] [varchar](255) NULL,
	City [varchar](50) NULL,
	State [varchar](50) NULL,
	Country [varchar](50) NULL,
	ZipCode [varchar](10) NULL,	
	[Cellphone] [varchar](20) NULL,
	[BusinessPhone] [varchar](20) NULL,
	[Email] [varchar](100)  NULL,
	[UserName]  [varchar](100) NOT NULL,
	[Password] [varchar](100) NOT NULL,
[notes] [varchar](255) NULL
 CONSTRAINT [pk_person] PRIMARY KEY CLUSTERED 
(
	[PersonId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO